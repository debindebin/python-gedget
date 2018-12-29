#/usr/bin/env python
#__*__coding: utf-8 __*__

import redis
import json

r = redis.Redis(host='113.127.83.151', port=6385, db=0, password='password')
# r1 = redis.Redis(host='112.126.82.150', port=6379, db=0, password='YiYi1011QAZ')
# obj1 = {'id':18, 'title':'瑜伽'}
# obj2 = {'id':26, 'title':'职场顾问'}
# obj3 = {'id':40, 'title':'化妆造型'}
# obj4 = {'id':17, 'title':'健身'}
# obj5 = {'id':34, 'title':'私厨/美食'}
# r.delete('SKILL_TAG_RECOMMAND')
# r.zadd('SKILL_TAG_RECOMMAND', json.dumps(obj1), 1)
# r.zadd('SKILL_TAG_RECOMMAND', json.dumps(obj2), 2)
# r.zadd('SKILL_TAG_RECOMMAND', json.dumps(obj3), 3)
# r.zadd('SKILL_TAG_RECOMMAND', json.dumps(obj4), 4)
# r.zadd('SKILL_TAG_RECOMMAND', json.dumps(obj5), 5)
#print json.dumps(obj1)
#print json.dumps(obj2)
#print json.dumps(obj3)
#s = r.get("REDIS_CATEGORY_LABEL18")
#s = s.replace("瑜伽", "")
#r.set("REDIS_CATEGORY_LABEL18", s)
# print r.zrange("SKILL_TAG_RECOMMAND", 0, -1)


# print r1.get('REDIS_CATEGORY_LABEL122')
# obj7=[{"id":1492137323273,"title":"名师课堂4.20"},{"id":1490265003574,"title":"名师课堂3.15"},{"id":1490265482639,"title":"名师课堂2.15  "},{"id":1490265516061,"title":"年度盛典"}]

homep1=r.get('HOME_PAGE_DEFINE_NEW')
# r.set('zdbTest11',homep1)
print homep1

# obj6={"nrChannelIds":[{"id":26,"title":"职场顾问","picUrl":"http://oa6vgpw61.bkt.clouddn.com/category/26.png","order":2},{"id":21,"title":"滑冰","picUrl":"http://oa6vgpw61.bkt.clouddn.com/category/21.png","order":21},{"id":23,"title":"羽毛球","picUrl":"http://oa6vgpw61.bkt.clouddn.com/category/23.png","order":21},{"id":73,"title":"手工","picUrl":"http://oa6vgpw61.bkt.clouddn.com/category/1468563300171.png","order":2147},{"id":18,"title":"瑜伽","picUrl":"http://oa6vgpw61.bkt.clouddn.com/category/18.png","order":21},{"id":82,"title":"篮球","picUrl":"http://oa6vgpw61.bkt.clouddn.com/category/1468563721198.png","order":214}],"guessList":[{"type":0,"picUrl":"http://oa6vgpw61.bkt.clouddn.com/home/1479264203748.jpg","id":1479264204658,"title":"能人直播","data":[{"skillType":2,"title":"哈他瑜伽人人夸编辑是吗那句号的就给我看见过exe","content":"第三届中国瑜伽私教大会暨中国瑜伽私教创新论坛广州站\u0026nbsp;2017-02-13\u0026nbsp;中国瑜...","picUrl":"http://oa6vgpw61.bkt.clouddn.com/lvb/2017/3/24/1490323867722.jpg","skillId":5820,"streamStart":"2017-02-24 10:40:00","nick":"何必占用","profileImageUrl":"http://oa6vgpw61.bkt.clouddn.com/head/2017/3/24/1490323654720.jpg","placeType":"1","segmentType":1,"lvbDuration":"0","order":2147483647,"mediaType":0,"lvbType":2},{"skillType":2,"title":"父亲微风","content":"","picUrl":"http://oa6vgpw61.bkt.clouddn.com/lvb/2016/12/28/1482924931588.jpg","skillId":5381,"streamStart":"2016-12-28 19:40:00","nick":"Gosivn","profileImageUrl":"http://oa6vgpw61.bkt.clouddn.com/head/2016/6_6/1465201776095.jpg","placeType":"1","segmentType":4,"lvbDuration":"0","order":2147483647,"mediaType":0,"lvbType":2},{"skillType":2,"title":"困难","content":"","picUrl":"http://oa6vgpw61.bkt.clouddn.com/lvb/2016/12/29/1482990319447.jpg","skillId":5384,"streamStart":"2016-12-29 13:45:23","nick":"朝阳","profileImageUrl":"http://oa6vgpw61.bkt.clouddn.com/profile/2017/3/29/1490770137349.jpg","placeType":"1","segmentType":1,"lvbDuration":"0","order":2147483647,"mediaType":0,"lvbType":1}]},{"type":0,"picUrl":"http://oa6vgpw61.bkt.clouddn.com/home/1479363310599.jpg","id":1479363311194,"title":"视听","data":[{"skillType":1,"title":"测试啊测试啊测试啊","content":"","picUrl":"http://oa6vgpw61.bkt.clouddn.com/activity/1487749520621.jpg","skillId":5984,"nick":"士且土","profileImageUrl":"http://oa6vgpw61.bkt.clouddn.com/head/2015/12_9/1449626528408.jpg","placeType":"1","videoLength":"180","order":2147483647,"mediaType":1},{"skillType":1,"title":"给我喂","content":"","picUrl":"http://oa6vgpw61.bkt.clouddn.com/microSkill/2016/08/03/1470216230767.jpg","skillId":3291,"nick":"回家睡觉","profileImageUrl":"http://oa6vgpw61.bkt.clouddn.com/head/2017/3/17/1489743350181.jpg","placeType":"1","videoLength":"10","order":2147483647,"mediaType":2},{"skillType":1,"title":"exe张83号发货想好好的","content":"","picUrl":"http://oa6vgpw61.bkt.clouddn.com/microSkill/2016/08/03/1470221598947.jpg","skillId":3306,"nick":"aaa6","profileImageUrl":"http://oa6vgpw61.bkt.clouddn.com/head/2016/6_16/1466043678482.png","placeType":"1","videoLength":"10","order":2147483647,"mediaType":2},{"skillType":1,"title":"哦ioooi","content":"","picUrl":"http://oa6vgpw61.bkt.clouddn.com/microSkill/2016/08/03/1470225632565.jpg","skillId":3325,"nick":"回家睡觉","profileImageUrl":"http://oa6vgpw61.bkt.clouddn.com/head/2017/3/17/1489743350181.jpg","placeType":"1","videoLength":"15","order":2147483647,"mediaType":2},{"skillType":1,"title":"测试购买","content":"exe疾控中心一心一意","picUrl":"http://oa6vgpw61.bkt.clouddn.com/microSkill/2016/5_19/1463624160724.jpg","skillId":1180,"nick":"花花1234","profileImageUrl":"http://oa6vgpw61.bkt.clouddn.com/head/2017/3/23/1490265064187.jpg","placeType":"1","videoLength":"2","order":2147483647,"mediaType":2},{"skillType":1,"title":"xnmxmx","content":"BBB","picUrl":"http://oa6vgpw61.bkt.clouddn.com/microSkill/2016/5_19/1463624762497.jpg","skillId":1182,"nick":"花花1234","profileImageUrl":"http://oa6vgpw61.bkt.clouddn.com/head/2017/3/23/1490265064187.jpg","placeType":"1","videoLength":"1","order":2147483647,"mediaType":2}]},{"type":0,"picUrl":"http://oa6vgpw61.bkt.clouddn.com/home/1479363325798.jpg","id":1479363325876,"title":"服务","data":[{"skillType":0,"title":"我为歌狂","content":"那些那些年继续看经典款笑口常开考察课看得开参考参考快下课的","picUrl":"http://oa6vgpw61.bkt.clouddn.com/skill/2016/3_18/1458270469425.jpg","skillId":454,"nick":"江左盟宗主","profileImageUrl":"http://oa6vgpw61.bkt.clouddn.com/head/2015/12_4/1449233407622.jpg","placeType":"1","city":"北京","district":"海淀","subDistrict":"双榆树","order":2147483647,"mediaType":0},{"skillType":0,"title":"纹身","content":"你是觉得就觉得就放假打击打击空姐日记非男非女","picUrl":"http://oa6vgpw61.bkt.clouddn.com/skill/2016/3_18/1458272694922.jpg","skillId":458,"nick":"mark","profileImageUrl":"http://oa6vgpw61.bkt.clouddn.com/head/2015/12_4/1449219896518.jpg","placeType":"3;2","city":"香港特别行政区","district":"中西","subDistrict":"","order":2147483647,"mediaType":0},{"skillType":0,"title":"平面模特","content":"很好，快来，哈哈哈哈哈哈哈哈哈","picUrl":"http://oa6vgpw61.bkt.clouddn.com/skill/2016/3_18/1458270700355.jpg","skillId":4720,"nick":"华仔","profileImageUrl":"http://oa6vgpw61.bkt.clouddn.com/head/2015/12_28/1451292292759.png","placeType":"2","order":2147483647,"mediaType":0},{"skillType":0,"title":"摄影","content":"好纠结啊看很多话不多见积极发挥到家","picUrl":"http://oa6vgpw61.bkt.clouddn.com/skill/2016/3_18/1458271738242.jpg","skillId":4721,"nick":"一米阳光","profileImageUrl":"http://oa6vgpw61.bkt.clouddn.com/head/2016/4_13/1460515586004.jpg","placeType":"2","city":"克朗代莱","district":"知春路","subDistrict":"","order":2147483647,"mediaType":0}]}]}

# r1.set('REDIS_CATEGORY_LABEL122',json.dumps(obj7, ensure_ascii=False))
# print r1.get('REDIS_CATEGORY_LABEL122')


# print r1.lrange('REDIS_LABEL_SKILL1490265003574',0,20)
