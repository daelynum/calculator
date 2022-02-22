from typing import List, Optional
from fastapi import FastAPI, status, Depends, HTTPException
import uvicorn
from database import Base, engine, get_db, Expressions
from sqlalchemy.orm import Session
from calculate_func import calculate_from_string
from schemas import Calculate

app = FastAPI()


@app.post('/calc', status_code=status.HTTP_201_CREATED, tags=['Service calculator'])
def calculate(request: str, db: Session = Depends(get_db)):
    try:
        """вариант для успешного выполнения функции"""
        result = calculate_from_string(request)
        new_expression = Expressions(request=request,
                                     response=result,
                                     status='success')

    except Exception as error:
        """вариант для выполнения функции с ошибкой
        По заданию строка в response должна быть пустой, мне показалось интереснее добавитьв нее описание ошибки"""
        new_expression = Expressions(request=request,
                                     response=str(error),
                                     status='fail')
    finally:
        db.add(new_expression)
        db.commit()
        db.refresh(new_expression)

    """удаляю первую строку из таблицы если кол-во строк превышает 30"""
    if db.query(Expressions).count() > 30:
        first_id_in_db = db.query(Expressions).all()[0].id
        removable_string = db.query(Expressions).filter(Expressions.id == first_id_in_db)
        removable_string.delete(synchronize_session=False)
        db.commit()
    return new_expression


@app.get('/history', response_model=List[Calculate], status_code=status.HTTP_200_OK, tags=['Service calculator'])
def show_history(limit: int = 30, response_status: Optional[str] = None, db: Session = Depends(get_db)):
    if (
        limit > 30
        or limit < 1
        or response_status is not None
        and response_status not in {'fail', 'success'}
    ):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    elif response_status is None:
        return db.query(Expressions).limit(limit).all()
    else:
        return db.query(Expressions).filter(Expressions.status == response_status).limit(limit).all()


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
    uvicorn.run(app, host='127.0.0.1', port=8000)
