from base64 import b64encode, b64decode
import dill

def serialize_function(function):
    # Pickle the function (use dill as usual
    # pickle doesn't work on locals/lambdas
    function = dill.dumps(function)
    # Convert to JSON-serialisable byte string
    function = b64encode(function)
    # Convert to plain string
    function = function.decode("utf-8")
    return function

def deserialize_function(function):
    function = b64decode(function)
    function = dill.loads(function)
    return function
