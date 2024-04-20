import os

# # This guide can only be run with the jax backend.
os.environ["KERAS_BACKEND"] = "jax"
# os.environ["KERAS_BACKEND"] = "tensorflow"

from typing import Union
import keras
import keras.ops as kops
from keras import Model, Input, Layer

from keras.layers import *


class ConvLayer(Layer):
    def __init__(
        self,
        num_filters: int = 16,
        kernel_size: int = 3,
        strides: int = 2,
        use_activation: bool = True,
        use_bn: bool = True,
        use_bias: bool = None,
        **kwargs,
    ):
        super().__init__(**kwargs)

        self.num_filters = num_filters
        self.kernel_size = kernel_size
        self.strides = strides
        self.num_filters = num_filters
        self.use_bn = use_bn
        self.use_activation = use_activation
        self.use_bias = use_bias if use_bias is not None else (False if self.use_bn else True)

        self.conv = Conv2D(filters=self.num_filters, kernel_size=self.kernel_size, strides=self.strides, padding="same", use_bias=self.use_bias)
        if self.use_bn:
            self.bn = BatchNormalization()

        if self.use_activation:
            self.activation = Activation("swish")

    def call(self, x, **kwargs):
        x = self.conv(x)
        if self.use_bn:
            x = self.bn(x)

        if self.use_activation:
            x = self.activation(x)

        return x


# https://github.com/apple/ml-cvnets/blob/84d992f413e52c0468f86d23196efd9dad885e6f/cvnets/modules/mobilevit_block.py#L186
# jax.
def unfolding(
    x,
    B: int = 1,
    D: int = 144,
    patch_h: int = 2,
    patch_w: int = 2,
    num_patches_h: int = 10,
    num_patches_w: int = 10,
):
    """
    ### Notations (wrt paper) ###
        B/b = batch
        P/p = patch_size
        N/n = number of patches
        D/d = embedding_dim

    H, W
    [                            [
        [1, 2, 3, 4],     Goal      [1, 3, 9, 11],
        [5, 6, 7, 8],     ====>     [2, 4, 10, 12],
        [9, 10, 11, 12],            [5, 7, 13, 15],
        [13, 14, 15, 16],           [6, 8, 14, 16]
    ]                            ]
    """
    print("B", B)
    # [B, H, W, D] --> [B*nh, ph, nw, pw*D]
    reshaped_fm = kops.reshape(x, (B * num_patches_h, patch_h, num_patches_w, patch_w * D))

    # [B*nh, ph, nw, pw*D] --> [B*nh, nw, ph, pw*D]
    transposed_fm = kops.transpose(reshaped_fm, axes=[0, 2, 1, 3])

    # [B*nh, nw, ph, pw*D] --> [B, N, P, D]
    reshaped_fm = kops.reshape(transposed_fm, (B, num_patches_h * num_patches_w, patch_h * patch_w, D))

    # [B, N, P, D] --> [B, P, N, D]
    transposed_fm = kops.transpose(reshaped_fm, axes=[0, 2, 1, 3])

    return transposed_fm


# https://github.com/apple/ml-cvnets/blob/84d992f413e52c0468f86d23196efd9dad885e6f/cvnets/modules/mobilevit_block.py#L233
def folding(
    x,
    B: int = 1,
    D: int = 144,
    patch_h: int = 2,
    patch_w: int = 2,
    num_patches_h: int = 10,
    num_patches_w: int = 10,
):
    """
    ### Notations (wrt paper) ###
        B/b = batch
        P/p = patch_size
        N/n = number of patches
        D/d = embedding_dim
    """
    # [B, P, N D] --> [B, N, P, D]
    x = kops.transpose(x, axes=(0, 2, 1, 3))

    # [B, N, P, D] --> [B*nh, nw, ph, pw*D]
    x = kops.reshape(x, (B * num_patches_h, num_patches_w, patch_h, patch_w * D))

    # [B*nh, nw, ph, pw*D] --> [B*nh, ph, nw, pw*D]
    x = kops.transpose(x, axes=(0, 2, 1, 3))

    # [B*nh, ph, nw, pw*D] --> [B, nh*ph, nw, pw, D] --> [B, H, W, C]
    x = kops.reshape(x, (B, num_patches_h * patch_h, num_patches_w * patch_w, D))

    return x


class MobileViT_v1_Block(Layer):
    def __init__(
        self,
        out_filters: int = 64,
        embedding_dim: int = 90,
        patch_size: Union[int, tuple] = (2, 2),
        transformer_repeats: int = 2,
        num_heads: int = 4,
        attention_drop: float = 0.0,
        linear_drop: float = 0.0,
        **kwargs,
    ):
        super().__init__(**kwargs)

        self.out_filters = out_filters
        self.embedding_dim = embedding_dim
        self.patch_size = patch_size
        self.transformer_repeats = transformer_repeats

        self.patch_size_h, self.patch_size_w = patch_size if isinstance(self.patch_size, tuple) else (self.patch_size // 2, self.patch_size // 2)
        # self.patch_size_h, self.patch_size_w = kops.cast(self.patch_size_h, dtype="int32"), kops.cast(self.patch_size_w, dtype="int32")

        # # local_feature_extractor 1 and 2
        self.local_rep_layers_1 = ConvLayer(num_filters=self.out_filters, kernel_size=3, strides=1, use_bn=True, use_activation=True)
        self.local_rep_layers_2 = ConvLayer(num_filters=self.embedding_dim, kernel_size=1, strides=1, use_bn=False, use_activation=False, use_bias=False)

        self.transformer_layer_norm = LayerNormalization(epsilon=1e-6)

        # Fusion blocks
        self.local_features_3 = ConvLayer(num_filters=self.out_filters, kernel_size=1, strides=1, use_bn=True, use_activation=True)
        self.concat = Concatenate(axis=-1)
        self.fuse_local_global = ConvLayer(num_filters=self.out_filters, kernel_size=3, strides=1, use_bn=True, use_activation=True)

    def call(self, x):

        print("x.shape", kops.shape(x), x.shape)

        # local_representation = self.local_rep(x)
        local_representation = self.local_rep_layers_1(x)
        local_representation = self.local_rep_layers_2(local_representation)

        # Transformer as Convolution Steps
        # --------------------------------
        # # Unfolding

        batch_size, fmH, fmW = kops.shape(x)[0], kops.shape(x)[1], kops.shape(x)[2]
        num_patches_h = kops.floor_divide(fmH, self.patch_size_h)
        num_patches_w = kops.floor_divide(fmW, self.patch_size_w)

        unfolded = unfolding(
            local_representation,
            B=batch_size,
            D=self.embedding_dim,
            patch_h=self.patch_size_h,
            patch_w=self.patch_size_w,
            num_patches_h=num_patches_h,
            num_patches_w=num_patches_w,
        )

        # print("here")

        # # Infomation sharing/mixing --> global representation
        global_representation = self.transformer_layer_norm(unfolded)

        # # Folding
        folded = folding(
            global_representation,
            B=batch_size,
            D=self.embedding_dim,
            patch_h=self.patch_size_h,
            patch_w=self.patch_size_w,
            num_patches_h=num_patches_h,
            num_patches_w=num_patches_w,
        )
        # # --------------------------------

        # Fusion
        local_mix = self.local_features_3(folded)
        fusion = self.concat([local_mix, x])
        fusion = self.fuse_local_global(fusion)

        return fusion
        # return x

    def get_config(self):
        config = super().get_config()
        config.update(
            {
                "out_filters": self.out_filters,
                "embedding_dim": self.embedding_dim,
                "patch_size": self.patch_size,
                "transformer_repeats": self.transformer_repeats,
            }
        )
        return config


def create_test_model():
    # Define input shape
    input_shape = (32, 32, 96)  # Assuming input shape is (32, 32, 96), adjust as necessary

    # Create input layer
    inputs = Input(shape=input_shape)

    print("inputs.shape", inputs.shape)
    mvitblk = MobileViT_v1_Block(
        out_filters=96,
        embedding_dim=144,
        transformer_repeats=2,
        name="MobileViTBlock-1",
        attention_drop=0.2,
        linear_drop=0.2,
    )(inputs)

    # Create model
    model = Model(inputs=inputs, outputs=mvitblk)

    # Print model summary
    model.summary()
    return model


if __name__ == "__main__":
    batch = 1
    H = W = 32
    C = 96
    P = 2 * 2
    L = 4
    embedding_dim = 144

    print("Testing layer initialization...")
    mvitblk = MobileViT_v1_Block(
        out_filters=96,
        embedding_dim=144,
        transformer_repeats=2,
        name="MobileViTBlock-1",
        attention_drop=0.2,
        linear_drop=0.2,
    )

    inputs = keras.random.normal((batch, H, W, C))

    out = mvitblk(inputs)
    print("inputs.shape", inputs.shape)
    print("out.shape", out.shape)

    print("-------------------------------------------\n" * 3)
    print("Testing layer inside Model.")
    # Test model creation
    create_test_model()
