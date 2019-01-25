# db2pojo
plain old java object generate tool from mysql database schema

### install
python 3 이상이 필요합니다.
```
$pip install db2pojo
```

### pojo 생성
```
$db2pojo --mysql-host $MYSQL-HOST --mysql-port $MYSQL-PORT --mysql-user $MYSQL-USER --mysql-password $MYSQL-PASSWORD --db-name $DB-NAME --table-names $TABLE1 $TABLE2... --pojo $OUTPUT-DIR $PACKAGE-NAME
```

### ddl script 생성
```
$db2pojo --mysql-host $MYSQL-HOST --mysql-port $MYSQL-PORT --mysql-user $MYSQL-USER --mysql-password $MYSQL-PASSWORD --db-name $DB-NAME --table-names $TABLE1 $TABLE2... --ddl $OUTPUT-DIR
```
