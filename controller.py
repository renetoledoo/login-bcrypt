from model import Pessoa
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import bcrypt

def session_return ():
    db = 'mysql+pymysql://root:1103@localhost:3306/logincli'
    engine = create_engine(db)
    Session = sessionmaker(bind=engine)
    return Session()

class ControllerCadastro():
    @classmethod
    def check_data(cls,name, email, pwd):
        if len(name) > 50 or len(name) < 3:
            return 2
        elif len(email) > 200:
            return 3
        elif len(name) >  100 or len(pwd) < 6:
            return 4
        else:
            return 1
        
    @classmethod
    def register(cls, name, email, pwd):
        session = session_return()
        user = session.query(Pessoa).filter(Pessoa.email == email).all()
        
        if len(user) > 0:
            return 5
        
        check = cls.check_data(name, email, pwd)
        
        if check != 1:
            return check
        try: 
            pwd_hashed = bcrypt.hashpw(pwd.encode('utf-8'), bcrypt.gensalt(10))
            p1 = Pessoa(name =name, email=email, pwd=pwd_hashed)
            session.add(p1)
            session.commit()
            return 1
        except Exception as e:
            print(e)


class ControllerLogin():
    @classmethod
    def login(cls, email, pwd):
        session = session_return()
        check_login = session.query(Pessoa).filter(Pessoa.email == email).all()
        
        if not check_login:
            return False
        
        pwd_hash = check_login[0].pwd  # Hash da senha armazenada no banco de dados
        if bcrypt.checkpw(pwd.encode('utf-8'), pwd_hash.encode('utf-8')):
            return {'logado': True, 'id': check_login[0].id}
        else:
            return False
        
        
        