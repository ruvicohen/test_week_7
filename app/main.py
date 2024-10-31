from flask import Flask

from app.db.database import engine, init_db
from app.db.models import Target, TargetType, City, Country, Mission

app = Flask(__name__)

# app.add_url_rule(
#     '/graphql',
#     view_func=GraphQLView.as_view(
#         'graphql',
#         schema=schema,
#         graphiql=True
#     )
# )


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')