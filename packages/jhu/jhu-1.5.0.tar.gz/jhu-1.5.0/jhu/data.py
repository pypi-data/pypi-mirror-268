from urllib.parse import quote_plus
from math import ceil
from typing import List
from sqlalchemy import func,Select
from sqlalchemy.orm.session import Session
# from sqlalchemy.sql.elements import BinaryExpression


class ORM:
    @staticmethod
    def build_engine_url(dialect_dbapi:str,host:str,port:str,username:str='',passwd:str='',database:str='',**kw)->str:
        """创建sqlalchemy的engine url
        
        Args:
            dialect_dbapi:数据库方言和数据库API,比如'pymsql+mysql','postgresql'
            host:主机地址
            port:端口号
            username:用户名
            passwd:密码
            database:数据库名
            **kw:数据库的参数
            
        Return:
            str: 返回格式为:dialect+dbapi://username:passwd@host:port/database?key=value&key=value
        """
        # 设置认证信息
        username, passwd = map(quote_plus, [username, passwd])
        auth_info = f'{username}:{passwd}' if passwd else username

        # 设置数据库信息
        database = f'/{database}' if database else ''

        # 设置参数信息
        if kw:
            args = '&'.join([f'{k}={kw[k]}' for k in kw])
            param = f'?{args}'
        else:
            param = ''

        # 拼接url
        url = f'{dialect_dbapi}://{auth_info}@{host}:{port}{database}{param}'
        return url

    @staticmethod
    def all(db:Session,stmt:Select)->List[dict]:
        """获取所有数据
        """
        ds = db.execute(stmt).mappings()
        return [dict(**data) for data in ds]
    
    
    @staticmethod
    def one(db:Session,stmt:Select)->dict|None:
        """获取第一行数据
        """
        ds = ORM.all(db,stmt)
        return ds[0] if ds else None

    @staticmethod
    def counts(db:Session,stmt:Select)->int:
        """获取数据量
        """
        return db.scalar(stmt.with_only_columns(func.count('1')))

    @staticmethod
    def pagination(db:Session,stmt:Select,page_idx:int=1,page_size:int=10,order:list=None)->dict:
        """分页查询数据
        """
        if page_size < 1:
            page_size = 1

        match(page_idx):
            case page_idx if page_idx > 0:
                offset = (page_idx - 1) * page_size
            case _:
                offset = 0
                page_idx = 1

        total = ORM.counts(db,stmt)
        page_total = ceil(total / page_size)

        pagination = dict(page_idx=page_idx, page_size=page_size,page_total=page_total,total=total)

        # 配置排序条件
        if order is not None:
            stmt = stmt.order_by(*order)

        # 配置分页条件
        stmt = stmt.offset(offset).limit(page_size)
        records = ORM.all(db,stmt)
        data=dict(records=records, pagination=pagination)
    
        return data