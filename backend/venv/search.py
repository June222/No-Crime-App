from flask_restful import reqparse, Resource
from crime import District
import pandas as pd

path = "file/real-crime-data/"

class SearchCrime(Resource): 
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('도.특별시.광역시')
        parser.add_argument('시.군.구')
        parser.add_argument('연도')
        
        args = parser.parse_args()
        argument_1 = args['도.특별시.광역시']
        argument_2 = args['시.군.구']
        argument_3 = args['연도']
        
        _year = pd.read_csv(path+argument_3+".csv", index_col = 0)
        
        try:
            district = District().district_name(argument_1, argument_2)
            _crime = _year[[district]].values.reshape(1,-1)[0]
            
            data = {
                "절도": str(_crime[0]),
                "살인": str(_crime[1]),
                "강도": str(_crime[2]),
                "성폭력": str(_crime[3]),
                "폭행": str(_crime[4])
            }
            return {"data": data}
        
        except:
            return {"message": "json으로 전달되는 body 형식이 잘못되었습니다."}
        
    