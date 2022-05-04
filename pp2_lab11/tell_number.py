import psycopg2
from config import database

config = psycopg2.connect(**database)
current = config.cursor()

def checkNum(number):
    if(number.find('8707') == 0 and len(number) == 11):
        return number
    elif(number.find('8747') == 0 and len(number) == 11):
        return number
    elif(number.find('8775') == 0 and len(number) == 11):
        return number
    elif(number.find('8708') == 0 and len(number) == 11):
        return number
    elif(number.find('8777') == 0 and len(number) == 11):
        return number
    elif(number.find('8778') == 0 and len(number) == 11):
        return number
    elif(number.find('8705') == 0 and len(number) == 11):
        return number
    print("Sorry, it seems you made a mistake in your phone number, can you write it again?")
    number = str(input())
    return checkNum(number)

def check(name):
    select = '''
            SELECT tell_num FROM telephone WHERE users_name = %s;
    '''
    current.execute(select, [name])
    DICT = current.fetchone()
    if DICT == None: return True
    else: return False


print("What's your query?")
print("1 - insert")
print("2 - delete")
print("3 - pagination")
print("4 - query")
query = int(input())

if(query == 1):
    #upgrade:
    # upd = '''
    #     create or replace procedure update(users_name_ varchar, tell_num_ varchar)
    #     as
    #     $$
    #         begin
    #             UPDATE telephone 
    #             SET tell_num = $2 
    #             WHERE users_name = $1;
    #         end;
    #     $$ language plpgsql;
    #     call update(%s, %s);
    # '''
    # insert:
    # ins = '''
    #     create or replace procedure insert(users_namee varchar, tell_nume varchar)
    #     as
    #     $$
    #         begin
    #             insert into telephone(users_name, tell_num) values ($1, $2);
    #         end; 
    #     $$ language plpgsql; 
    #     call insert(%s,%s); 
    # '''

    print("How many people you want to add?")
    n = int(input())
    for _ in range(0,n):
        print("Enter user name:")
        name = str(input())
        print("Enter user phone number:")
        number = str(input())
        number = checkNum(number)
        if(check(name)): 
            current.execute("call insert(%s,%s);", (name,number))
        else:
            current.execute("call update(%s, %s);",(name,number))
        

if(query == 2):
     #delete:
    # dele = '''
    #     create or replace procedure delete(data varchar)
    #     as
    #     $$
    #         begin
    #             delete from telephone where users_name = $1  or tell_num = $1; 
    #         end;
    #     $$ language plpgsql;
    #     call delete(%s);
    # '''

    data = str(input())
    current.execute("call delete(%s);", [data])
       

if(query == 3):
    print("type your limit and offset")
    limit = int(input())
    offset = int(input())
    pa = '''
        select * from telephone offset %s limit %s;
    '''
    current.execute(pa ,(limit,offset))
    print(current.fetchall())


if(query == 4):
    #querying:
    # que = '''
    #     create or replace function querying(data varchar)
    #         returns table (
    #             users_name varchar,
    #             tell_num varchar
    #         )
    #     as
    #     $$
    #         begin
    #             return query
    #                 select * from telephone where users_name ilike $1 or tell_num ilike $1;
    #         end;
    #     $$ language plpgsql;
    #     select querying(%s)
    # '''

    pat = str(input())
    current.execute("select querying(%s)" ,["%"+pat+"%"])
    print(current.fetchall())

current.close()
config.commit()
config.close()