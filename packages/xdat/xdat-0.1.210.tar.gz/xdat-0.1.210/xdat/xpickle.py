import cloudpickle
try:
    import keras
    from keras.models import load_model
except ImportError:
    keras = None

from io import BytesIO

class XCloudPickler(cloudpickle.CloudPickler):
    def save(self, obj, save_persistent_id=True):
        if keras is not None and isinstance(obj, keras.Model):
            # Handle Keras model serialization
            with BytesIO() as buffer:
                keras.models.save_model(obj, buffer, save_format='h5')
                keras_model_data = buffer.getvalue()
            self.write(cloudpickle.CloudPickler.save_reduce(self, load_keras_model_from_bytes, (keras_model_data,), obj=obj))
        else:
            # Fallback to default behavior
            super().save(obj, save_persistent_id=save_persistent_id)

def load_keras_model_from_bytes(data):
    with BytesIO(data) as buffer:
        return load_model(buffer)

def x_dump(obj, file):
    XCloudPickler(file).dump(obj)


def monkey_patch():
    cloudpickle.__dump_orig = cloudpickle.dump
    cloudpickle.dump = x_dump
