from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Session

class Base(DeclarativeBase):
    pass

class Address_kr(Base):
    __tablename__ = "address_kr"
    id: Mapped[int] = mapped_column(primary_key=True)
    siNm : Mapped[str] = mapped_column(String(40))
    sggNm : Mapped[str] = mapped_column(String(40))
    roadNm : Mapped[str] = mapped_column(String(80))

    def __repr__(self) -> str:
        return f"<Address_kr (siNm={self.siNm!r}, sggNm={self.sggNm!r}, roadNm={self.roadNm!r})>"

engine = create_engine("sqlite:///src/roadname.db", echo=True)

Base.metadata.create_all(engine)

with Session(engine) as session :
    try :
        f = open(f'src/addr/TN_SPRD_RDNM.txt', 'r', encoding='cp949')
        for line in f.readlines() : 
            siNm = line.split('|')[5]
            sggNm = line.split('|')[6]
            roadNm = line.split('|')[3]

            new_road = Address_kr(siNm=siNm, 
                                sggNm=sggNm, 
                                roadNm=roadNm)
            session.add_all([new_road])
        f.close()
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")
    session.commit()
