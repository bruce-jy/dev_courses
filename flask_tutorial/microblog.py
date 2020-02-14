from app import app, db, cli
from app.models import User, Post

# flask shell 에서 call 할 수 있도록 세팅한다.
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
