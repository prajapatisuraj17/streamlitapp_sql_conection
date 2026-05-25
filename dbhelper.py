   

class Db:

        def __init__(self): 
            import mysql.connector

            try:
                self.conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='root123',
                database='indigo',
                auth_plugin='mysql_native_password' # Force compatibility
                       )
                print('connection succesful')
                self.mycursor=self.conn.cursor(buffered=True)
            except:
                 print('connection fail')  


        def fetch_city_name(self):
                 self.mycursor.execute("""
                select source from flights
                union                    
                select Destination from flights
                   """)
                 data=self.mycursor.fetchall()
                 print(data)
                 city=[] 
                 for i in data:
                       city.append(i[0])
                 return city          

        def flight_df(self,source,destination):
              self.mycursor.execute("""
                 select Airline,Source,Destination,Total_Stops,Price from flights
                 where Source ='{}' and Destination='{}'                    
             """.format(source,destination))
              data=self.mycursor.fetchall()
              return data
        
        def fetch_pie_data(self):
              airline=[]
              freq=[]
              self.mycursor.execute("""

                       Select Airline,count(*)  from flights
                       group by Airline             
                       """)
              result=self.mycursor.fetchall()
              for item in result:
                    airline.append(item[0])
                    freq.append(item[1])
              return airline,freq

        def data_for_chart(self):
             city=[]
             freq=[]
             self.mycursor.execute("""
                      select source, count(*) from (select source from flights
                                                    union all
                                                    select destination from flights) t
                                                    group by t.source
                                                    order by count(*) desc
                                                """)
             result=self.mycursor.fetchall() 
             for item in result:
                   city.append(item[0])
                   freq.append(item[1])
             return city,freq