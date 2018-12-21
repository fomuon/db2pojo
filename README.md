# db2pojo
plain old java object generate tool from mysql database schema

### pojo 생성
```
cli.py --mysql-host $MYSQL-HOST --mysql-port $MYSQL-PORT --mysql-user $MYSQL-USER --mysql-password $MYSQL-PASSWORD --db-name $DB-NAME --table-names $TABLE1 $TABLE2... --pojo $OUTPUT-DIR $PACKAGE-NAME
```

### ddl script 생성
```
cli.py --mysql-host $MYSQL-HOST --mysql-port $MYSQL-PORT --mysql-user $MYSQL-USER --mysql-password $MYSQL-PASSWORD --db-name $DB-NAME --table-names $TABLE1 $TABLE2... --ddl $OUTPUT-DIR
```
