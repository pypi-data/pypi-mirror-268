import json
from inhand.service.MQSender import RabbitMQ
class PushMessage:
    """
        private String locale = "English";
    private String Title;
    //消息内容
    private String short_content;
    private String content;
    //app push的id
    private List<String> app_tag_list;
    private List<String> app_alias_list;

    private String audience;
    private List<String> phone_list;
    private List<String> email_list;
    private List<String> im_list;
    private Map<String,Object> params;

    """
    locale: str = "English"
    title: str = None
    short_content: str = None
    content: str = None
    app_tag_list: list = []
    app_alias_list: list = []
    audience: str = None
    phone_list: list = []
    email_list: list = []
    im_list: list = []
    params: dict = {}

    def toDict(self):
        kv= {
            'locale': self.locale,
            'title': self.title,
            'short_content': self.short_content,
            'content': self.content,
            'app_tag_list': self.app_tag_list,
            'app_alias_list': self.app_alias_list,
            'audience': self.audience,
            'phone_list': self.phone_list,
            'email_list': self.email_list,
            'im_list': self.im_list,
            'params': self.params
        }
        return kv

    def toJson(self):
        return json.dumps(self.toDict())

    @staticmethod
    def send(mq_sender: RabbitMQ, exchange:str, routing_key:str, message: PushMessage):
        mq_sender.send_message(exchange,routing_key,message.toJson())