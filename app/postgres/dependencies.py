from fastapi import Request

"""
Database Dependencies for application
"""


async def get_db(request: Request):
    Session = request.app.state.db_session_factory

    session_local = Session()
    try:
        yield session_local
    except Exception as e:
        await session_local.rollback()
        raise e
    finally:
        await session_local.close()
