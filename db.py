from sqlmodel import SQLModel, create_engine


engine = create_engine("postgresql://postgres:postgres@localhost/postgres")

def init_db():
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)
