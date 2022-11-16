### For start a project
`docker-compose up`

### Example endpoints
#### Get city
`curl -XGET 'http://localhost:5001/api/v1/city/<cityId>'`

#### Add city
`curl -XPOST -H "Content-type: application/json" -d '{"cityName":"Paris"}' 'http://localhost:5001/api/v1/city'`

#### Delete city
`curl -XDELETE 'http://localhost:5001/api/v1/city/<cityId>'`

#### Get all cities
`curl -XGET 'http://localhost:5001/api/v1/cities'`

#### Find 2 nearest cities
`curl -XGET 'http://localhost:5001/api/v1/findTheNearest?latitude=43.5&longitude=45.4'`
