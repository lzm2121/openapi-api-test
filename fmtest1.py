import cloudapitestbase
import logging
import jsonschema
logger = logging.getLogger()

resp_schema_play_res={
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "resources": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "duration": {
              "type": "integer"
            },
            "music_album_name": {
              "type": "string"
            },
            "music_cover_url": {
              "type": "string"
            },
            "music_name": {
              "type": "string"
            },
            "music_singer": {
              "type": "string"
            },
            "play_count": {
              "type": "integer"
            },
            "playable": {
              "type": "integer"
            },
            "res_content": {
              "type": "string"
            },
            "res_id": {
              "type": "string"
            }
          },
          "required": [
            "duration",
            "music_album_name",
            "music_cover_url",
            "music_name",
            "music_singer",
            "play_count",
            "playable",
            "res_content",
            "res_id"
          ]
        },
        {
          "type": "object",
          "properties": {
            "duration": {
              "type": "integer"
            },
            "music_album_name": {
              "type": "string"
            },
            "music_cover_url": {
              "type": "string"
            },
            "music_name": {
              "type": "string"
            },
            "music_singer": {
              "type": "string"
            },
            "play_count": {
              "type": "integer"
            },
            "playable": {
              "type": "integer"
            },
            "res_content": {
              "type": "string"
            },
            "res_id": {
              "type": "string"
            }
          },
          "required": [
            "duration",
            "music_album_name",
            "music_cover_url",
            "music_name",
            "music_singer",
            "play_count",
            "playable",
            "res_content",
            "res_id"
          ]
        },
        {
          "type": "object",
          "properties": {
            "duration": {
              "type": "integer"
            },
            "music_album_name": {
              "type": "string"
            },
            "music_cover_url": {
              "type": "string"
            },
            "music_name": {
              "type": "string"
            },
            "music_singer": {
              "type": "string"
            },
            "play_count": {
              "type": "integer"
            },
            "playable": {
              "type": "integer"
            },
            "res_content": {
              "type": "string"
            },
            "res_id": {
              "type": "string"
            }
          },
          "required": [
            "duration",
            "music_album_name",
            "music_cover_url",
            "music_name",
            "music_singer",
            "play_count",
            "playable",
            "res_content",
            "res_id"
          ]
        },
        {
          "type": "object",
          "properties": {
            "duration": {
              "type": "integer"
            },
            "music_album_name": {
              "type": "string"
            },
            "music_cover_url": {
              "type": "string"
            },
            "music_name": {
              "type": "string"
            },
            "music_singer": {
              "type": "string"
            },
            "play_count": {
              "type": "integer"
            },
            "playable": {
              "type": "integer"
            },
            "res_content": {
              "type": "string"
            },
            "res_id": {
              "type": "string"
            }
          },
          "required": [
            "duration",
            "music_album_name",
            "music_cover_url",
            "music_name",
            "music_singer",
            "play_count",
            "playable",
            "res_content",
            "res_id"
          ]
        },
        {
          "type": "object",
          "properties": {
            "duration": {
              "type": "integer"
            },
            "music_album_name": {
              "type": "string"
            },
            "music_cover_url": {
              "type": "string"
            },
            "music_name": {
              "type": "string"
            },
            "music_singer": {
              "type": "string"
            },
            "play_count": {
              "type": "integer"
            },
            "playable": {
              "type": "integer"
            },
            "res_content": {
              "type": "string"
            },
            "res_id": {
              "type": "string"
            }
          },
          "required": [
            "duration",
            "music_album_name",
            "music_cover_url",
            "music_name",
            "music_singer",
            "play_count",
            "playable",
            "res_content",
            "res_id"
          ]
        },
        {
          "type": "object",
          "properties": {
            "duration": {
              "type": "integer"
            },
            "music_album_name": {
              "type": "string"
            },
            "music_cover_url": {
              "type": "string"
            },
            "music_name": {
              "type": "string"
            },
            "music_singer": {
              "type": "string"
            },
            "play_count": {
              "type": "integer"
            },
            "playable": {
              "type": "integer"
            },
            "res_content": {
              "type": "string"
            },
            "res_id": {
              "type": "string"
            }
          },
          "required": [
            "duration",
            "music_album_name",
            "music_cover_url",
            "music_name",
            "music_singer",
            "play_count",
            "playable",
            "res_content",
            "res_id"
          ]
        }
      ]
    }
  },
  "required": [
    "resources"
  ]
}

resp_schema_switch_next={
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "res_info": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "duration": {
              "type": "integer"
            },
            "music_album_name": {
              "type": "string"
            },
            "music_cover_url": {
              "type": "string"
            },
            "music_name": {
              "type": "string"
            },
            "music_singer": {
              "type": "string"
            },
            "offset_milliseconds": {
              "type": "integer"
            },
            "play_count": {
              "type": "integer"
            },
            "playable": {
              "type": "integer"
            },
            "res_content": {
              "type": "string"
            },
            "res_id": {
              "type": "string"
            },
            "res_type": {
              "type": "integer"
            }
          },
          "required": [
            "duration",
            "music_album_name",
            "music_cover_url",
            "music_name",
            "music_singer",
            "offset_milliseconds",
            "play_count",
            "playable",
            "res_content",
            "res_id",
            "res_type"
          ]
        },
        {
          "type": "object",
          "properties": {
            "duration": {
              "type": "integer"
            },
            "music_album_name": {
              "type": "string"
            },
            "music_cover_url": {
              "type": "string"
            },
            "music_name": {
              "type": "string"
            },
            "music_singer": {
              "type": "string"
            },
            "offset_milliseconds": {
              "type": "integer"
            },
            "play_count": {
              "type": "integer"
            },
            "playable": {
              "type": "integer"
            },
            "res_content": {
              "type": "string"
            },
            "res_id": {
              "type": "string"
            },
            "res_type": {
              "type": "integer"
            }
          },
          "required": [
            "duration",
            "music_album_name",
            "music_cover_url",
            "music_name",
            "music_singer",
            "offset_milliseconds",
            "play_count",
            "playable",
            "res_content",
            "res_id",
            "res_type"
          ]
        },
        {
          "type": "object",
          "properties": {
            "duration": {
              "type": "integer"
            },
            "music_album_name": {
              "type": "string"
            },
            "music_cover_url": {
              "type": "string"
            },
            "music_name": {
              "type": "string"
            },
            "music_singer": {
              "type": "string"
            },
            "offset_milliseconds": {
              "type": "integer"
            },
            "play_count": {
              "type": "integer"
            },
            "playable": {
              "type": "integer"
            },
            "res_content": {
              "type": "string"
            },
            "res_id": {
              "type": "string"
            },
            "res_type": {
              "type": "integer"
            }
          },
          "required": [
            "duration",
            "music_album_name",
            "music_cover_url",
            "music_name",
            "music_singer",
            "offset_milliseconds",
            "play_count",
            "playable",
            "res_content",
            "res_id",
            "res_type"
          ]
        },
        {
          "type": "object",
          "properties": {
            "duration": {
              "type": "integer"
            },
            "music_album_name": {
              "type": "string"
            },
            "music_cover_url": {
              "type": "string"
            },
            "music_name": {
              "type": "string"
            },
            "music_singer": {
              "type": "string"
            },
            "offset_milliseconds": {
              "type": "integer"
            },
            "play_count": {
              "type": "integer"
            },
            "playable": {
              "type": "integer"
            },
            "res_content": {
              "type": "string"
            },
            "res_id": {
              "type": "string"
            },
            "res_type": {
              "type": "integer"
            }
          },
          "required": [
            "duration",
            "music_album_name",
            "music_cover_url",
            "music_name",
            "music_singer",
            "offset_milliseconds",
            "play_count",
            "playable",
            "res_content",
            "res_id",
            "res_type"
          ]
        },
        {
          "type": "object",
          "properties": {
            "duration": {
              "type": "integer"
            },
            "music_album_name": {
              "type": "string"
            },
            "music_cover_url": {
              "type": "string"
            },
            "music_name": {
              "type": "string"
            },
            "music_singer": {
              "type": "string"
            },
            "offset_milliseconds": {
              "type": "integer"
            },
            "play_count": {
              "type": "integer"
            },
            "playable": {
              "type": "integer"
            },
            "res_content": {
              "type": "string"
            },
            "res_id": {
              "type": "string"
            },
            "res_type": {
              "type": "integer"
            }
          },
          "required": [
            "duration",
            "music_album_name",
            "music_cover_url",
            "music_name",
            "music_singer",
            "offset_milliseconds",
            "play_count",
            "playable",
            "res_content",
            "res_id",
            "res_type"
          ]
        },
        {
          "type": "object",
          "properties": {
            "duration": {
              "type": "integer"
            },
            "music_album_name": {
              "type": "string"
            },
            "music_cover_url": {
              "type": "string"
            },
            "music_name": {
              "type": "string"
            },
            "music_singer": {
              "type": "string"
            },
            "offset_milliseconds": {
              "type": "integer"
            },
            "play_count": {
              "type": "integer"
            },
            "playable": {
              "type": "integer"
            },
            "res_content": {
              "type": "string"
            },
            "res_id": {
              "type": "string"
            },
            "res_type": {
              "type": "integer"
            }
          },
          "required": [
            "duration",
            "music_album_name",
            "music_cover_url",
            "music_name",
            "music_singer",
            "offset_milliseconds",
            "play_count",
            "playable",
            "res_content",
            "res_id",
            "res_type"
          ]
        }
      ]
    },
    "tts": {
      "type": "string"
    }
  },
  "required": [
    "res_info",
    "tts"
  ]
}
class TestFM(cloudapitestbase.CloudApiTestBase):
    #获取播放资源
    def test_play_res(self):
        res = self.api.FM_play_res()
        print(res)
        jsonschema.validate(res, resp_schema_play_res)

    #获取收藏列表
    def test_get_fav_list(self):
        res = self.api.FM("get_fav_list")
        print(res)
        jsonschema.validate(res, resp_schema_play_res)

    #换一个
    def test_switch_next(self):
        res = self.api.FM("switch_next")
        print(res)
        jsonschema.validate(res, resp_schema_switch_next)

    #根据资源id查询播放的节目信息
    def test_get_res_detail(self):
        res = self.api.FM("get_res_detail")
        print(res)
        jsonschema.validate(res, resp_schema_play_res)

    #预拉取更多
    def test_pre_get_more(self):
        res = self.api.FM("pre_get_more")
        print(res)
        jsonschema.validate(res, resp_schema_play_res)

    #收藏，取消收藏 缺少必要的请求参数
    def test_set_fav(self):
        res = self.api.FM_set_fav()
        print(res)

