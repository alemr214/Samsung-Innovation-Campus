import tensorflow as tf

print(f"GPUs disponibles {tf.config.list_physical_devices('GPU')}")
