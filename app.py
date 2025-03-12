import json
import os

def handler(event, context):
    app = {}
    
    countries = [
      {
        'id': 1,
        'name': 'Ghana',
      },
      {
        'id': 2,
        'name': 'France',
      },
      {
        'id': 3,
        'name': 'Scotland',
      },
    ]
    
    names = [
      {
        'name': 'Harry Potter',
        'city': 'London',
      },
      {
        'name': 'Don Quixote',
        'city': 'Madrid',
      },
      {
        'name': 'Joan of Arc',
        'city': 'Paris',
      },
      {
        'name': 'Rosa Park',
        'city': 'Alabama',
      },
    ]
    
    todos = [
      {
        'title': 'Clean the kitchen',
        'description':
          'Mop the floor, wipe the countertop and don\'t forget to take out the trash!',
      },
      {
        'title': 'Call Mom',
        'description': 'It\'s her birthday!',
      },
      {
        'title': 'Water flowers',
        'description': 'They need water, or they will die.',
      },
    ]
    
    def home(event, context):
        response = {
            'statusCode': 200,
            'body': json.dumps({'message': 'API is Online!'}),
            'headers': {
                'Content-Type': 'application/json',
            },
        }
        return response
    
    def get_countries(event, context):
        response = {
            'statusCode': 200,
            'body': json.dumps({'data': countries}),
            'headers': {
                'Content-Type': 'application/json',
            },
        }
        return response
    
    def get_names(event, context):
        response = {
            'statusCode': 200,
            'body': json.dumps({'data': names}),
            'headers': {
                'Content-Type': 'application/json',
            },
        }
        return response
    
    def get_todos(event, context):
        response = {
            'statusCode': 200,
            'body': json.dumps({'data': todos}),
            'headers': {
                'Content-Type': 'application/json',
            },
        }
        return response
    
    app['/'] = {
        'GET': home,
    }
    app['/countries'] = {
        'GET': get_countries,
    }
    app['/names'] = {
        'GET': get_names,
    }
    app['/todos'] = {
        'GET': get_todos,
    }
    
    path = event['path']
    http_method = event['httpMethod']
    
    if path not in app or http_method not in app[path]:
        response = {
            'statusCode': 404,
            'body': json.dumps({'message': 'Resource not found'}),
            'headers': {
                'Content-Type': 'application/json',
            },
        }
        return response
    
    return app[path][http_method](event, context)