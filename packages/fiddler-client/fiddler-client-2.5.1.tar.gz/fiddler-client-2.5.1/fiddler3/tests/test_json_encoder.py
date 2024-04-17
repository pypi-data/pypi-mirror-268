from uuid import UUID

import pytest
import simplejson

from fiddler3.libs.json_encoder import RequestClientJSONEncoder


def test_json_encoder_uuid():
    data = {'uuid_field': UUID('6ea7243e-0bf7-4323-ba1b-9f788b4a9257')}
    with pytest.raises(TypeError):
        simplejson.dumps(data)

    assert simplejson.dumps(data, cls=RequestClientJSONEncoder) == simplejson.dumps(
        {'uuid_field': '6ea7243e-0bf7-4323-ba1b-9f788b4a9257'}
    )
