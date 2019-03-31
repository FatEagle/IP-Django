# 挖优笔记API - DEMO


## 搜索
使用Elasticsearch作为后端进行搜索, 具体实现是让想要被检索的对象使用继承了SearchSerializer的Serializer. 这样在对象进行创建和更新时, SearchSerializer会调用to_representation()在这里进行对Elasticsearch的文档的创建与删除.

### Elasticsearch的初始化配置
需要对每一个需要存储在Elasticsearch的类创建一个index, 并对index做mapping, 以使得文档支持中文搜索.

#### Mapping的模板
==拼音分词器有bug==, 不适用于长文本

Tokenizer使用了 IK Analysis对文本进行中文分词, 其有两种模式:
* ik_smart: 粗粒度
* ik_max_word: 细粒度

Token filter使用了pinyin, 将词转换为拼音全拼和首字母,如:
    信息 --> xinxi, xx

以下模板是先对文本进行ik_max_word模式的中文分词
```
PUT IndexName
{
    "index": {
        "analysis": {
            "analyzer": {
                "ik_pinyin_analyzer": {
                    "type": "custom",
                    "tokenizer": "ik_max_word",
                    "filter": ["my_pinyin", "word_delimiter"]
                }
            },
            "filter": {
                "my_pinyin": {
                    "type" : "pinyin",
                    "keep_full_pinyin" : false,
                    "keep_joined_full_pinyin": true,
                    "keep_none_chinese": true,
                    "keep_none_chinese_together": true,
                    "none_chinese_pinyin_tokenize": false
                }
            }
        }
    }
}
```