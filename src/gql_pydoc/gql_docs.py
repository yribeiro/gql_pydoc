# Module containing various queries to get schema information

introspection_query = """{
    __schema{
        queryType{
            name
            fields{
                name
                description
            }
        }
    }
}"""
