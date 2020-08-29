import pymongo as pm
import datetime


fh = open("Vocabulary_set.csv", "r")
wd_list = fh.readlines()

wd_list.pop(0)

vocab_list = []

for rawstring in wd_list:
    word , defination = rawstring.split(',' , 1 )
    defination = defination.rstrip()
    vocab_list.append({'word': word,  'defination': defination})


#print(vocab_list)

client = pm.MongoClient("mongodb://localhost:27017/")
db = client['vocab']


dbs = client.list_database_names()
vocab_col = db["vocab_list"]
vocab_col.drop()


vocab_dict = {'word': 'cryptic', 'defination': 'secret with hidden meaning'}
res = vocab_col.insert_one(vocab_dict)
print('Insert Id: ', res.inserted_id)

if "vocab" in dbs:
    print("Database Exists")

res = vocab_col.insert_many(vocab_list)

#print(res.inserted_ids)

data = vocab_col.find_one()
print(data)

for data in vocab_col.find({}, {"__id":0 , "defination":0}):
    print(data)

data = vocab_col.find_one({'word': 'boistrerous'})
print(data)

upd = vocab_col.update_one({'word': 'boisterous'},{'$set':{'defination':"rowdy;noisy"}})
print('modified count:', upd.modified_count)

print(data)


upd = vocab_col.update_many({}, {'$set':{'last_updated UTC:': datetime.datetime.utcnow().strftime('%Y-%m-%d%H%M%SZ')}})
print('modified_count: ', upd.modified_count)