# RoboCupDBA
## Exmaple Insert RoboCupDBA
```
import RoboCupDBA
RoboCupDBA.Insert(link="mongodb://root:6yHnmju%26@localhost:27017/",db="data",collection="data",name="1",x=0.0,y=0.0,theta=0.0,typeObj="A")
```
>```link``` is **mongodb link** for mongodb.

>```db``` is **database account** for mongodb.

>```collection``` is *** collection account** for mongodb.

>```name``` is **Fill data name location ** for mongodb. [String]

>```x``` is **Fill data name location x-axis ** for mongodb. [Dobule]

>```y``` is **Fill data name location y-axis** from mongodb. [Dobule]

>```theta``` is **Fill data name location theta ** from mongodb. [Dobule]

>```typeObj``` is **Type Object RoboCup** from mongodb. [String]

* function RoboCupDBA.Insert can ```retrun True``` is Connect success. if ```retrun False``` is disconnect or Connect false.


## Exmaple Query RoboCupDBA
```
import RoboCupDBA
RoboCupDBA.Query(link="mongodb://root:6yHnmju%26@localhost:27017/",db="data",collection="data",json={"_id":'1'})
```
>```link``` is **mongodb link** for mongodb.

>```db``` is **database account** for mongodb.

>```collection``` is *** collection account** for mongodb.

>```json``` is **Fill data json query ** for mongodb. [String]

* function RoboCupDBA.Query can ```retrun Value Query``` is Connect success. if ```retrun False``` is disconnect or Connect false.
