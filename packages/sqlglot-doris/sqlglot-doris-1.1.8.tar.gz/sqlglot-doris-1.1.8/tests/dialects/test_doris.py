from tests.dialects.test_dialect import Validator


class TestDoris(Validator):
    dialect = "doris"

    def test_doris(self):
        self.validate_all(
            "SELECT number FROM NUMBERS('number' = '15')",
            read={
                "clickhouse": "SELECT number FROM NUMBERS(15)",
            },
        )
        self.validate_all(
            "SELECT x FROM tbl",
            read={
                "clickhouse": "SELECT x FROM tbl FINAL",
            },
        )
        self.validate_all(
            "COUNT(DISTINCT x)",
            read={
                "clickhouse": "countdistinct(x)",
            },
        )
        self.validate_all(
            "MIN(CASE WHEN user_id = 42 THEN timestamp ELSE NULL END)",
            read={
                "clickhouse": "minif(timestamp, user_id = 42)",
            },
        )
        self.validate_all(
            "CASE WHEN left < right THEN 'left is smaller' WHEN left > right THEN 'left is greater' WHEN left = right THEN 'Both equal' ELSE 'Null value' END",
            read={
                "clickhouse": "multiIf(left < right, 'left is smaller', left > right, 'left is greater', left = right, 'Both equal', 'Null value')",
            },
        )
        self.validate_all(
            "SELECT LOCATE(LOWER('a'), LOWER('abc')) IN b",
            read={
                "clickhouse": "SELECT positionCaseInsensitiveUTF8('abc','a') Global in b",
            },
        )
        self.validate_all(
            "SELECT TO_DATE('2020-02-02 00:00:00')",
            write={
                "doris": "SELECT TO_DATE('2020-02-02 00:00:00')",
                "oracle": "SELECT CAST('2020-02-02 00:00:00' AS DATE)",
            },
        )
        self.validate_all(
            "SELECT Approx_Quantile(x,1)",
            write={
                "doris": "SELECT PERCENTILE_APPROX(x, 1)",
            },
        )
        self.validate_all(
            "SELECT PERCENTILE_APPROX(x, 1)",
            read={
                "starrocks": "SELECT PERCENTILE_APPROX_RAW(x,1)",
            },
        )
        self.validate_all(
            "PERCENTILE_APPROX(x, 1)",
            read={
                "spark": "approx_percentile(x, 1)",
            },
        )
        self.validate_all(
            "SELECT MAX_BY(a, b), MIN_BY(c, d)",
            read={"clickhouse": "SELECT argMax(a, b), argMin(c, d)"},
        )
        self.validate_all(
            "SELECT ARRAY_JOIN(ARRAY('a', 'b', 'c', NULL),'#')",
            read={"postgres": "SELECT array_to_string(['a','b','c',null],'#')"},
        )
        self.validate_all(
            "SELECT ARRAY_JOIN(ARRAY('a', 'b', 'c', NULL),'#','*')",
            read={"postgres": "SELECT array_to_string(['a','b','c',null],'#','*')"},
        )
        self.validate_all(
            "SELECT CONCAT_WS('',ARRAY('12/05/2021', '12:50:00')) AS DateString",
            read={
                "clickhouse": "SELECT arrayStringConcat(['12/05/2021', '12:50:00']) AS DateString"
            },
        )
        self.validate_all(
            "SELECT CONCAT_WS('*', ARRAY('12/05/2021', '12:50:00')) AS DateString",
            read={
                "clickhouse": "SELECT arrayStringConcat(['12/05/2021', '12:50:00'], '*') AS DateString"
            },
        )
        self.validate_all(
            "${a}",
            read={"presto": "${a}"},
        )

        self.validate_all(
            "SELECT aa, sum(CASE WHEN index_name = 'ceshi' THEN score ELSE 0 END) AS avg_score FROM table GROUP BY aa",
            read={
                "presto": "select aa,sum(score) filter(where index_name='ceshi') as avg_score from table group by aa"
            },
        )

        self.validate_all(
            "SELECT CAST('2024-01-16' AS STRING)",
            read={"clickhouse": "SELECT TOSTRING('2024-01-16')"},
        )
        self.validate_all(
            "SELECT HOURS_DIFF(CAST('2018-01-02 23:00:00' AS DATETIME), CAST('2018-01-01 22:00:00' AS DATETIME))",
            read={
                "clickhouse": "SELECT dateDiff('hour', toDateTime('2018-01-01 22:00:00'), toDateTime('2018-01-02 23:00:00'));"
            },
        )
        self.validate_all(
            "${a}",
            read={"presto": "${a}"},
        )

        self.validate_all(
            "SELECT aa, sum(CASE WHEN index_name = 'ceshi' THEN score ELSE 0 END) AS avg_score FROM table GROUP BY aa",
            read={
                "presto": "select aa,sum(score) filter(where index_name='ceshi') as avg_score from table group by aa"
            },
        )

        self.validate_all(
            "REPLACE('www.baidu.com:9090','9090','')",
            read={
                # "clickhouse": "REPLACEALL('www.baidu.com:9090','9090','')",
                "presto": "REPLACE('www.baidu.com:9090','9090')",
                "clickhouse": "replaceAll('www.baidu.com:9090','9090','')",
            },
        )
        self.validate_all(
            "SELECT TO_DATE('2022-12-30 01:02:03')",
            read={"clickhouse": "SELECT toDate('2022-12-30 01:02:03')"},
        )
        self.validate_all(
            "SELECT YEAR(a), QUARTER(a), MONTH(a), HOUR(a), MINUTE(a), SECOND(a), UNIX_TIMESTAMP(a)",
            read={
                "clickhouse": "SELECT toYear(a), toQuarter(a),toMonth(a), toHour(a), toMinute(a), toSecond(a), toUnixTimestamp(a)"
            },
        )
        self.validate_all(
            "SELECT YEARS_ADD(x, 1), MONTHS_ADD(x, 1), WEEKS_ADD(x, 1), DAYS_ADD(x, 1), HOURS_ADD(x, 1), SECONDS_ADD(x, 1), MONTHS_ADD(x,3)",
            read={
                "clickhouse": "SELECT  addYears(x, 1), addMonths(x, 1), addWeeks(x, 1), addDays(x, 1), addHours(x, 1), addSeconds(x, 1), addQuarters(x, 1)"
            },
        )
        self.validate_all(
            "SELECT YEARS_SUB(x, 1), MONTHS_SUB(x, 1), SECONDS_SUB(x, 1), MONTHS_SUB(x,3)",
            read={
                "clickhouse": "SELECT  subtractYears(x, 1), subtractMonths(x, 1), subtractSeconds(x, 1), subtractQuarters(x, 1)"
            },
        )
        self.validate_all(
            "SELECT DATE_SUB(x, INTERVAL 1 WEEK), DATE_SUB(x, INTERVAL 1 HOUR), DATE_SUB(x, INTERVAL 1 DAY), DATE_SUB(x, INTERVAL 1 MINUTE)",
            read={
                "clickhouse": "SELECT  subtractweeks(x, 1), subtracthours(x, 1), subtractdays(x, 1), subtractminutes(x, 1)"
            },
        )
        self.validate_all(
            "SELECT DATE_FORMAT(x, '%Y%m'), DATE_FORMAT(x, '%Y%m%d'), DATE_FORMAT(x, '%Y%m%d%H%i%s'), DATE_TRUNC(x, 'Quarter'), DATE_TRUNC(x, 'Month'), DATE_TRUNC(x, 'Week'), DATE_TRUNC(x, 'Day'), DATE_TRUNC(x, 'Hour'), DATE_TRUNC(x, 'Minute'), DATE_TRUNC(x, 'Second')",
            read={
                "clickhouse": "SELECT toYYYYMM(x, 'US/Eastern'), toYYYYMMDD(x, 'US/Eastern'), toYYYYMMDDHHMMSS(x, 'US/Eastern'), toStartOfQuarter(x),  toStartOfMonth(x), toStartOfWeek(x), toStartOfDay(x), toStartOfHour(x), toStartOfMinute(x), toStartOfSecond(x)"
            },
        )

        self.validate_all(
            "SHA2(x,256)",
            read={
                "presto": "SHA256(x)",
            },
        )
        self.validate_all(
            "NULL_OR_EMPTY('')",
            read={
                "clickhouse": "empty('')",
            },
        )
        self.validate_all(
            "NOT_NULL_OR_EMPTY('')",
            read={
                "clickhouse": "NotEmpty('')",
            },
        )
        self.validate_all(
            "CHAR_LENGTH('x')",
            read={
                "clickhouse": "lengthUTF8('x')",
            },
        )
        self.validate_all(
            "MONTHS_ADD(d, n)",
            read={
                "oracle": "ADD_MONTHS(d, n)",
            },
            write={
                "doris": "MONTHS_ADD(d, n)",
                "oracle": "ADD_MONTHS(d, n)",
            },
        )
        self.validate_all(
            "IF(0 < 1, True, Null)",
            read={
                "spark": "ASSERT_TRUE(0 < 1)",
            },
        )
        self.validate_all("CAST(x AS DOUBLE)", read={"clickhouse": "toFloat64OrNull(x)"})

    def test_identity(self):
        self.validate_identity("COALECSE(a, b, c, d)")
        self.validate_identity("SELECT CAST(`a`.`b` AS INT) FROM foo")
        self.validate_identity("SELECT APPROX_COUNT_DISTINCT(a) FROM x")
        self.validate_identity("ARRAY_SORT(x)", "ARRAY_SORT(x)")
        self.validate_identity("DATE_ADD(x,1)", "DATE_ADD(x, INTERVAL 1 DAY)")
        self.validate_identity("DATE_SUB(x,1)", "DATE_SUB(x, INTERVAL 1 DAY)")
        self.validate_identity("DATEDIFF(x,1)", "DATEDIFF(x, 1)")
        self.validate_identity("GROUP_ARRAY(x)", "COLLECT_LIST(x)")
        self.validate_identity("NOW()", "NOW()")
        self.validate_identity("SIZE(x)", "ARRAY_SIZE(x)")
        self.validate_identity("SPLIT_BY_STRING(x,',')", "SPLIT_BY_STRING(x, ',')")
        self.validate_identity("3&5", "BITAND(3, 5)")
        self.validate_identity("3|5", "BITOR(3, 5)")
        self.validate_identity("3^5", "BITXOR(3, 5)")
        self.validate_identity("~5", "BITNOT(5)")
        self.validate_identity("random(2)", "FLOOR(RANDOM()*2.0)")
        self.validate_identity("random(2,3)", "FLOOR(RANDOM()*1.0+2.0)")
        self.validate_identity("a||b", "CONCAT(a,b)")
        self.validate_identity(
            "select * from t where comment Match_Any 'OLAP'",
            "SELECT * FROM t WHERE comment MATCH_ANY 'OLAP'",
        )
        self.validate_identity(
            "select * from t where comment Match_All 'OLAP'",
            "SELECT * FROM t WHERE comment MATCH_ALL 'OLAP'",
        )
        self.validate_identity(
            "select * from t where comment MATCH_PHRASE 'OLAP'",
            "SELECT * FROM t WHERE comment MATCH_PHRASE 'OLAP'",
        )

    def test_time(self):
        self.validate_all("DAYOFMONTH(x)", read={"clickhouse": "toDayOfMonth(x)"})
        self.validate_all("DAYOFYEAR(x)", read={"clickhouse": "toDayOfYear(x)"})
        self.validate_all("DAYOFWEEK(x)", read={"clickhouse": "toDayOfWeek(x)"})
        self.validate_all("INTERVAL x SECOND", read={"clickhouse": "toIntervalSecond(x)"})
        self.validate_all("INTERVAL x MINUTE", read={"clickhouse": "toIntervalMinute(x)"})
        self.validate_all("INTERVAL x HOUR", read={"clickhouse": "toIntervalHour(x)"})
        self.validate_all("INTERVAL x DAY", read={"clickhouse": "toIntervalDay(x)"})
        self.validate_all("INTERVAL x WEEK", read={"clickhouse": "toIntervalWeek(x)"})
        self.validate_all("INTERVAL x MONTH", read={"clickhouse": "toIntervalMonth(x)"})
        self.validate_all("INTERVAL (3 * x) MONTH", read={"clickhouse": "toIntervalQuarter(x)"})
        self.validate_all("INTERVAL x YEAR", read={"clickhouse": "toIntervalYear(x)"})
        self.validate_all(
            "DATE_ADD(TO_DATE('2018-01-01'), INTERVAL '3' YEAR)",
            read={
                "clickhouse": "addDate(toDate('2018-01-01'), INTERVAL 3 YEAR)",
            },
        )
        self.validate_all(
            "DATE_SUB(TO_DATE('2018-01-01'), INTERVAL '3' YEAR)",
            read={
                "clickhouse": "subDate(toDate('2018-01-01'), INTERVAL 3 YEAR)",
            },
        )
        self.validate_all(
            "DATE_FORMAT(CAST('2002-04-20 17:31:12.66' AS DATETIME), '%h:%i:%S')",
            read={
                "postgres": "to_char(timestamp '2002-04-20 17:31:12.66', 'HH12:MI:SS')",
            },
        )
        self.validate_identity("TIMESTAMP('2022-01-01')")
        self.validate_all(
            "WEEK(CAST('2010-01-01' AS DATE), 3)",
            read={
                "presto": "week(DATE '2010-01-01')",
            },
        )
        self.validate_all(
            "DATE_FORMAT(FROM_UNIXTIME(1609167953694 / 1000), '%Y-%m-%d')",
            read={
                "presto": "format_datetime(from_unixtime(1609167953694/1000),'yyyy-MM-dd')",
            },
        )
        self.validate_all(
            "FROM_UNIXTIME(s.send_time, '%Y%m%d')",
            read={
                "hive": " from_timestamp(s.send_time,'yyyyMMdd')",
            },
        )
        self.validate_all(
            "DATE_SUB(TO_DATE('2018-01-01'), INTERVAL 3 YEAR)",
            read={"clickhouse": "date_sub(YEAR, 3, toDate('2018-01-01'))"},
        )
        self.validate_all(
            "DATE_SUB(TO_DATE('2018-01-01'), INTERVAL '1' MONTH)",
            read={
                "clickhouse": "date_sub(toDate('2018-01-01'), interval 1 month)",
            },
        )
        self.validate_all(
            "DATE_TRUNC(NOW(), 'day')",
            read={
                "hive": "TRUNC(current_timestamp(), 'DD')",
                "oracle": "TRUNC(current_timestamp(), 'DD')",
            },
        )
        self.validate_all(
            "NOW()",
            read={
                "hive": "SYSDATE",
                "oracle": "SYSDATE",
                "redshift": "SYSDATE",
            },
        )
        self.validate_all(
            "DATE_FORMAT(CAST('2022-08-20 08:23:42' AS DATETIME), '%Y-%m-%d %H:%i:%s')",
            read={
                "presto": "format_datetime(TIMESTAMP '2022-08-20 08:23:42', 'yyyy-mm-dd hh24:mi:ss')"
            },
        )
        self.validate_all(
            "DATE_FORMAT(x, '%Y')",
            read={"presto": "to_date(x,'yyyy') "},
        )
        self.validate_all(
            "DATE_FORMAT(x, '%Y-%m-%d %H:%i:%s')",
            read={"presto": "to_date(x,'yyyy-mm-dd hh24:mi:ss')"},
        )
        self.validate_all(
            "DATE_TRUNC(t, 'year')",
            read={
                "spark": "date_trunc(t,'YEAR')",
            },
        )
        self.validate_all(
            "DATE_TRUNC(t, 'Year')",
            read={
                "clickhouse": "toStartOfInterval(t, INTERVAL 1 year)",
            },
        )
        self.validate_all(
            "DATE_TRUNC(t, 'month')",
            read={
                "spark": "DATE_TRUNC(t, 'MM')",
            },
        )
        self.validate_all(
            "DATE_TRUNC(t, 'day')",
            read={
                "spark": "DATE_TRUNC(t, 'DD')",
            },
        )
        self.validate_all(
            "DATE_TRUNC(t, 'hour')",
            read={
                "spark": "DATE_TRUNC(t, 'HOUR')",
            },
        )
        self.validate_all(
            "MONTHS_DIFF(a, b)",
            read={"spark": "months_between(a, b)"},
        )
        self.validate_all(
            "CONVERT_TZ(CAST('2016-08-31' AS DATETIME),'UTC','Asia/Seoul')",
            read={
                "spark": "from_utc_timestamp('2016-08-31', 'Asia/Seoul')",
            },
        )
        self.validate_all(
            "STR_TO_DATE('2005-01-01 13:14:20', '%Y-%m-%d %H:%i:%s')",
            read={"oracle": "to_date('2005-01-01 13:14:20','yyyy-MM-dd hh24:mi:ss')"},
        )
        self.validate_all(
            "STR_TO_DATE('2005-01-01 13:14:20', '%Y-%m-%d %H:%i:%s')",
            read={"oracle": "to_date('2005-01-01 13:14:20','yyyy-mm-dd hh24:mi:ss')"},
        )
        self.validate_all(
            "STR_TO_DATE('1981-01-23 00:00:00', '%Y-%m-%d %H:%i:%s')",
            read={"oracle": "TO_DATE('1981-01-23 00:00:00', 'SYYYY-MM-DD HH24:MI:SS')"},
        )
        self.validate_all(
            "DATE_FORMAT(DATE_TRUNC(NOW(), 'Month'), '%Y-%m-%d')",
            read={
                "clickhouse": "formatDateTime(toStartOfMonth(now()),'%Y-%m-%d')",
            },
        )
        self.validate_all(
            "DATE_ADD(TO_DATE('2018-01-01'), INTERVAL '3' MONTH)",
            read={
                "clickhouse": "timestamp_add(toDate('2018-01-01'), INTERVAL 3 MONTH)",
            },
        )
        self.validate_all(
            "DATE_SUB(CAST('2018-12-18 01:02:03' AS DATETIME), INTERVAL 5 MONTH)",
            read={
                "clickhouse": "timestamp_sub(MONTH, 5, toDateTime('2018-12-18 01:02:03'))",
            },
        )

    def test_regex(self):
        self.validate_all(
            "SELECT REGEXP_LIKE(abc, '%foo%')",
            write={
                "doris": "SELECT REGEXP(abc, '%foo%')",
            },
        )

        self.validate_all(
            "SELECT REGEXP_EXTRACT('Abcd abCd aBcd', '(ab.)', 1)",
            read={
                "postgres": "SELECT regexp_match('Abcd abCd aBcd', 'ab.')",
                "presto": "SELECT REGEXP_EXTRACT('Abcd abCd aBcd', 'ab.')",
            },
        )

        self.validate_all(
            "SELECT REGEXP_EXTRACT_ALL('abcd abcd abcd', '(ab.)')",
            read={
                "postgres": "SELECT regexp_matches('abcd abcd abcd', 'ab.')",
                "clickhouse": "SELECT extractAll('abcd abcd abcd', 'ab.')",
                "presto": "SELECT REGEXP_EXTRACT_ALL('abcd abcd abcd', 'ab.')",
            },
        )
        self.validate_all(
            "REGEXP_REPLACE_ONE('Hello, World!', '.*', '*****')",
            read={
                "clickhouse": "replaceRegexpOne('Hello, World!', '.*', '*****')",
            },
        )

    def test_array(self):
        self.validate_all(
            "ARRAY_CONCAT(ARRAY(1, 2), ARRAY(3, 4), ARRAY(5, 6))",
            read={
                "clickhouse": "arrayConcat([1, 2], [3, 4], [5, 6])",
            },
        )
        self.validate_all(
            "ARRAY_REVERSE_SORT(ARRAY(1, 2, 3))",
            read={
                "clickhouse": "arrayReverse([1, 2, 3])",
            },
        )
        self.validate_all(
            "ARRAY_REVERSE_SORT(ARRAY(1, 2, 3))",
            read={
                "clickhouse": "Reverse([1, 2, 3])",
            },
        )
        self.validate_all(
            "ARRAYS_OVERLAP(ARRAY(1, 2, 3, 4), ARRAY(5, 6, 7))",
            read={
                "clickhouse": "hasany([1, 2,3, 4], [5,6,7])",
            },
        )
        self.validate_all(
            "ARRAY_COUNT(ARRAY(12, 33, 5))",
            read={
                "clickhouse": "arrayCount(ARRAY(12, 33, 5))",
            },
        )
        self.validate_all(
            "ARRAY_ENUMERATE_UNIQ(ARRAY(1, 1, 1, 2, 2, 2), ARRAY(1, 1, 2, 1, 1, 2))",
            read={
                "clickhouse": "arrayEnumerateUniq(ARRAY(1, 1, 1, 2, 2, 2), ARRAY(1, 1, 2, 1, 1, 2))",
            },
        )
        self.validate_all(
            "SELECT SIZE(ARRAY_DISTINCT(x))",
            read={"clickhouse": "SELECT ARRAYUNIQ(x)"},
        )
        self.validate_all(
            "ARRAY_SORT(x)",
            read={
                "clickhouse": "ARRAYSORT(x)",
            },
        )
        self.validate_all(
            "ARRAY_MAP(x -> x + 1, ARRAY(5, 6))",
            read={"presto": "transform(ARRAY [5, 6], x -> x + 1)"},
        )
        self.validate_all(
            "SELECT ARRAY_POPBACK(ARRAY(1, 2, 3))",
            read={
                "clickhouse": "select arrayPopBack([1, 2, 3])",
            },
        )
        self.validate_all(
            "SELECT ARRAY_POPFRONT(ARRAY(1, 2, 3))",
            read={
                "clickhouse": "select  arrayPopFront([1, 2, 3])",
            },
        )
        self.validate_all(
            "SELECT ARRAY_PUSHBACK(ARRAY(1, 2, 3), 4)",
            read={
                "clickhouse": "select arrayPushBack([1, 2, 3], 4)",
                "postgres": "select ARRAY_APPEND([1, 2, 3], 4)",
            },
        )
        self.validate_all(
            "SELECT ARRAY_PUSHFRONT(ARRAY(1, 2, 3), 4)",
            read={
                "clickhouse": "select arrayPushFront([1, 2, 3], 4)",
                "postgres": "select ARRAY_PREPEND(4, [1, 2, 3])",
            },
        )
        self.validate_all(
            "ARRAY_SLICE(ARRAY(1, 2, NULL, 4, 5), 2, 3)",
            read={
                "clickhouse": "arraySlice([1, 2, NULL, 4, 5], 2, 3) ",
            },
        )
        self.validate_all(
            "ARRAY_CONTAINS(ARRAY(1, 2, NULL), NULL)",
            read={
                "clickhouse": "has([1, 2, NULL], NULL) ",
            },
        )
        self.validate_all(
            "ARRAY_RANGE(0, 5)",
            read={
                "clickhouse": "range(0, 5) ",
                "presto": "sequence(0, 4)",
            },
        )
        self.validate_all(
            "ARRAY_SHUFFLE(x)",
            read={
                "presto": "Shuffle(x)",
            },
        )
        self.validate_all(
            "ARRAY_SLICE(ARRAY(1, 2, 3), 1)",
            read={
                "presto": "slice([1,2,3],1)",
            },
        )
        self.validate_all(
            "ELEMENT_AT(ARRAY(1, 2, 3), 1)",
            read={
                "clickhouse": "arrayElement([1, 2, 3],1)",
            },
        )
        self.validate_all(
            "ARRAY_POSITION(ARRAY(1, 3, NULL, NULL), NULL)",
            read={
                "clickhouse": "indexOf([1, 3, NULL, NULL], NULL)",
            },
        )
        self.validate_all("arr_int[1]", read={"presto": "element_at(arr_int, 1)"})
        self.validate_all(
            "SELECT ARRAY_AVG(ARRAY(1, 2, 4))",
            read={"clickhouse": "SELECT arrayAvg([1, 2, 4]);"},
        )
        self.validate_all(
            "SELECT ARRAY_COMPACT(ARRAY(1, 1, 2, 3, 3, 3))",
            read={"clickhouse": "SELECT arrayCompact([1, 1, 2, 3, 3, 3])"},
        )
        self.validate_all(
            "SELECT ARRAY_CUM_SUM(ARRAY(1, 1, 1, 1))",
            read={"clickhouse": "SELECT arrayCumSum(ARRAY(1, 1, 1, 1))"},
        )
        self.validate_all(
            "SELECT ARRAY_DIFFERENCE(ARRAY(1, 2, 3, 4))",
            read={"clickhouse": "SELECT arrayDifference([1, 2, 3, 4])"},
        )
        self.validate_all(
            "SELECT ARRAY_DISTINCT(ARRAY(1, 2, 2, 3, 1))",
            read={"clickhouse": "SELECT arrayDistinct([1, 2, 2, 3, 1])"},
        )
        self.validate_all(
            "SELECT ARRAY_EXISTS(x -> x > 1, ARRAY(1, 2, 3))",
            read={"clickhouse": "SELECT arrayexists(x->x>1,[1,2,3])"},
        )
        self.validate_all(
            "SELECT ARRAY_FILTER(x -> x LIKE '%World%',ARRAY('Hello', 'abc World')) AS res",
            read={
                "clickhouse": "SELECT arrayFilter(x -> x LIKE '%World%', ['Hello', 'abc World']) AS res"
            },
        )
        self.validate_all(
            "SELECT ARRAY_FIRST(x -> x > 2, ARRAY(1, 2, 3, 0))",
            read={"clickhouse": "select arrayfirst(x->x>2, [1,2,3,0])"},
        )
        self.validate_all(
            "SELECT ARRAY_FIRST_INDEX(x -> x + 1 > 3, ARRAY(2, 3, 4))",
            read={"clickhouse": "select arrayFirstIndex(x->x+1>3, [2, 3, 4])"},
        )
        self.validate_all(
            "SELECT ARRAY_INTERSECT(ARRAY(1, 2), ARRAY(1, 3))",
            read={"clickhouse": "SELECT arrayIntersect([1, 2], [1, 3])"},
        )
        self.validate_all(
            "SELECT ARRAY_LAST(x -> x > 2, ARRAY(1, 2, 3, 0))",
            read={"clickhouse": "select arrayLast(x->x>2, [1,2,3,0])"},
        )
        self.validate_all(
            "SELECT ARRAY_LAST_INDEX(x -> x + 1 > 3, ARRAY(2, 3, 4))",
            read={"clickhouse": "select arrayLastIndex(x->x+1>3, [2, 3, 4])"},
        )
        self.validate_all(
            "SELECT ARRAY_MAP(x -> (x + 2), ARRAY(1, 2, 3)) AS res",
            read={"clickhouse": "SELECT arrayMap(x -> (x + 2), [1, 2, 3]) as res"},
        )
        self.validate_all(
            "SELECT ARRAY_PRODUCT(ARRAY(1, 2, 3, 4, 5, 6))",
            read={"clickhouse": "SELECT arrayProduct([1,2,3,4,5,6])"},
        )
        self.validate_all(
            "SELECT ARRAY_REVERSE_SORT(ARRAY('hello', 'world', '!'))",
            read={"clickhouse": "SELECT arrayReverseSort(['hello', 'world', '!'])"},
        )
        self.validate_all(
            "SELECT ARRAY_SUM(x -> x * x, ARRAY(2, 3))",
            read={
                "clickhouse": "SELECT arraySum(x -> x*x, [2, 3])",
            },
            write={
                "clickhouse": "SELECT arraySum(x -> x * x, [2, 3])",
                "doris": "SELECT ARRAY_SUM(x -> x * x, ARRAY(2, 3))",
            },
        )
        self.validate_all(
            "SELECT SIZE(ARRAY_DISTINCT(ARRAY(1, 1, 2, 3, 3, 3)))",
            read={"clickhouse": "SELECT arrayUniq([1, 1, 2, 3, 3, 3])"},
        )
        self.validate_all(
            "SELECT ARRAY_ZIP(ARRAY('a', 'b', 'c'), ARRAY(5, 2, 1))",
            read={"clickhouse": "SELECT arrayZip(['a', 'b', 'c'], [5, 2, 1])"},
        )
        self.validate_all(
            "SELECT ARRAY_ZIP(ARRAY('a', 'b', 'c'), ARRAY(5, 2, 1))",
            read={"clickhouse": "SELECT arrayZip(['a', 'b', 'c'], [5, 2, 1])"},
        )
        self.validate_all(
            "COLLECT_LIST(res)",
            read={"clickhouse": " groupArray(res)"},
        )
        self.validate_all(
            "LAST_DAY(x)",
            read={
                "clickhouse": " toLastDayOfMonth(x)",
                "presto": " last_day_of_month(x)",
            },
        )
        self.validate_all(
            "ARRAY_CONCAT(ARRAY(1), ARRAY(2, 3))",
            read={
                "clickhouse": "flatten([1], [2, 3])",
            },
        )
        self.validate_all(
            "ARRAY_ENUMERATE(x)",
            read={
                "clickhouse": "arrayEnumerate(x)",
            },
        )

    def test_bitmap(self):
        self.validate_all(
            "BITMAP_FROM_ARRAY(ARRAY(1, 2, 3, 4, 5))",
            read={
                "clickhouse": "bitmapBuild([1, 2, 3, 4, 5]) ",
            },
        )
        self.validate_all(
            "BITMAP_TO_ARRAY(BITMAP_FROM_ARRAY(ARRAY(1, 2, 3, 4, 5)))",
            read={
                "clickhouse": "bitmapToArray(bitmapBuild([1, 2, 3, 4, 5])) ",
            },
        )
        self.validate_all(
            "BITMAP_AND(a, b)",
            read={
                "clickhouse": "bitmapAnd(a,b)",
            },
        )
        self.validate_all(
            "BITMAP_AND_COUNT(a, b)",
            read={
                "clickhouse": "bitmapAndCardinality(a,b)",
            },
        )
        self.validate_all(
            "BITMAP_AND_NOT(a, b)",
            read={
                "clickhouse": "bitmapAndnot(a,b)",
            },
        )
        self.validate_all(
            "BITMAP_AND_NOT_COUNT(a, b)",
            read={
                "clickhouse": "bitmapAndnotCardinality(a,b)",
            },
        )
        self.validate_all(
            "BITMAP_COUNT(BITMAP_FROM_ARRAY(ARRAY(1, 2, 3, 4, 5)))",
            read={
                "clickhouse": "bitmapCardinality(bitmapBuild([1, 2, 3, 4, 5]))",
            },
        )
        self.validate_all(
            "BITMAP_CONTAINS(BITMAP_FROM_ARRAY(ARRAY(1, 5, 7, 9)), 9)",
            read={
                "clickhouse": "bitmapContains(bitmapBuild([1,5,7,9]), 9)",
            },
        )
        self.validate_all(
            "BITMAP_OR_COUNT(a, b)",
            read={
                "clickhouse": "bitmapOrCardinality(a, b)",
            },
        )
        self.validate_all(
            "BITMAP_XOR_COUNT(a, b)",
            read={
                "clickhouse": "bitmapXorCardinality(a, b)",
            },
        )
        self.validate_all(
            "BITMAP_HAS_ANY(a, b)",
            read={
                "clickhouse": "bitmapHasAny(a, b)",
            },
        )
        self.validate_all(
            "BITMAP_HAS_ALL(a, b)",
            read={
                "clickhouse": "bitmapHasAll(a, b)",
            },
        )

    def test_bit(self):
        self.validate_all(
            "BITMAP_MAX(BITMAP_FROM_ARRAY(ARRAY(1, 2, 3, 4, 5)))",
            read={
                "clickhouse": "bitmapMax(bitmapBuild([1, 2, 3, 4, 5]))",
            },
        )
        self.validate_all(
            "BITMAP_MIN(BITMAP_FROM_ARRAY(ARRAY(1, 2, 3, 4, 5)))",
            read={
                "clickhouse": "bitmapMin(bitmapBuild([1, 2, 3, 4, 5]))",
            },
        )
        self.validate_all(
            "BIT_COUNT(333)",
            read={
                "clickhouse": "bitCount(333)",
            },
        )
        self.validate_all(
            "BITMAP_TO_ARRAY(BITMAP_SUBSET_IN_RANGE(BITMAP_FROM_ARRAY(ARRAY(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 100, 200, 500)), 30, 200))",
            read={
                "clickhouse": "bitmapToArray(bitmapSubsetInRange(bitmapBuild([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,100,200,500]), 30, 200))"
            },
        )
        self.validate_all(
            "BITMAP_TO_ARRAY(BITMAP_SUBSET_LIMIT(BITMAP_FROM_ARRAY(ARRAY(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 100, 200, 500)), CAST(30 AS INT), CAST(200 AS INT)))",
            read={
                "clickhouse": "bitmapToArray(bitmapSubsetLimit(bitmapBuild([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,100,200,500]), toInt32(30), toInt32(200)))"
            },
        )
        self.validate_all(
            "BITMAP_TO_ARRAY(SUB_BITMAP(BITMAP_FROM_ARRAY(ARRAY(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 100, 200, 500)), CAST(10 AS INT), CAST(10 AS INT)))",
            read={
                "clickhouse": "bitmapToArray(subBitmap(bitmapBuild([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,100,200,500]), toInt32(10), toInt32(10)))"
            },
        )
        self.validate_all(
            "GROUP_BIT_AND(x)",
            read={
                "postgres": "BIT_AND(x)",
                "clickhouse": "GROUPBITAND(x)",
                "snowflake": "BITAND_AGG(x)",
            },
        )
        self.validate_all(
            "GROUP_BIT_OR(x)",
            read={
                "postgres": "BIT_OR(x)",
                "clickhouse": "GROUPBITOR(x)",
                "snowflake": "BITOR_AGG(x)",
            },
        )
        self.validate_all(
            "GROUP_BIT_XOR(x)",
            read={
                "postgres": "BIT_XOR(x)",
                "clickhouse": "GROUPBITXOR(x)",
                "snowflake": "BITXOR_AGG(x)",
            },
        )
        self.validate_all(
            "BIT_SHIFT_RIGHT(CAST('7' AS TINYINT), 2)",
            read={
                "presto": "bitwise_right_shift(TINYINT '7', 2)",
                "trino": "bitwise_right_shift(TINYINT '7', 2)",
                "clickhouse": "bitShiftRight(CAST('7' AS TINYINT), 2)",
            },
        )
        self.validate_all(
            "BIT_SHIFT_LEFT(CAST('-7' AS TINYINT), 2)",
            read={
                "presto": "bitwise_left_shift(TINYINT '-7', 2)",
                "trino": "bitwise_left_shift(TINYINT '-7', 2)",
                "clickhouse": "bitShiftLeft(CAST('-7' AS TINYINT), 2)",
            },
        )

    def test_ip(self):
        self.validate_all(
            "IPV4_STRING_TO_NUM_OR_DEFAULT(addr)",
            read={
                "clickhouse": "IPv4StringToNumOrDefault(addr)",
            },
        )
        self.validate_all(
            "IPV6_STRING_TO_NUM_OR_DEFAULT(addr)",
            read={
                "clickhouse": "IPv6StringToNumOrDefault(addr)",
            },
        )
        self.validate_all(
            "IS_IPV4_STRING(addr)",
            read={
                "clickhouse": "IsIPv4String(addr)",
            },
        )
        self.validate_all(
            "IS_IPV6_STRING(addr)",
            read={
                "clickhouse": "IsIPv6String(addr)",
            },
        )
        self.validate_all(
            "IPV4_NUM_TO_STRING(addr)",
            read={
                "clickhouse": "IPv4NumToString(addr)",
            },
        )
        self.validate_all(
            "IPV4_STRING_TO_NUM(addr)",
            read={
                "clickhouse": "IPv4StringToNum(addr)",
            },
        )
        self.validate_all(
            "IPV6_STRING_TO_NUM(addr)",
            read={
                "clickhouse": "IPv6StringToNum(addr)",
            },
        )
        self.validate_all(
            "TO_IPV4(addr)",
            read={
                "clickhouse": "toIPv4(addr)",
            },
        )
        self.validate_all(
            "TO_IPV6(addr)",
            read={
                "clickhouse": "toIPv6(addr)",
            },
        )
        self.validate_all(
            "IPV4_STRING_TO_NUM(addr)",
            read={
                "clickhouse": "IPv4StringToNum(addr)",
            },
        )

    def test_varchar(self):
        self.validate_all(
            "AES_DECRYPT(UNHEX('24E9E4966469'),'123456789101213141516171819202122','iviviviviviviviv123456')",
            read={
                "clickhouse": "aes_decrypt_mysql('aes-256-ofb', unhex('24E9E4966469'), '123456789101213141516171819202122', 'iviviviviviviviv123456')",
            },
        )
        self.validate_all(
            "AES_ENCRYPT('Secret','12345678910121314151617181920212','iviviviviviviviv')",
            read={
                "clickhouse": "aes_encrypt_mysql('aes-256-ofb', 'Secret', '12345678910121314151617181920212', 'iviviviviviviviv')",
            },
        )
        self.validate_all(
            "UUID()",
            read={
                "clickhouse": "generateUUIDv4()",
            },
        )
        self.validate_all(
            "CAST(CONCAT(x,y) AS STRING)",
            read={
                "postgres": " to_char(x||y)",
            },
        )
        self.validate_all(
            "LOCATE('a', 'abc')",
            read={
                "presto": "index('abc','a')",
                "clickhouse": "position('abc','a')",
                "postgres": "strpos('abc','a')",
            },
        )
        self.validate_all(
            "LOCATE('a', 'abc')",
            read={
                "clickhouse": "positionUTF8('abc','a')",
            },
        )
        self.validate_all(
            "LOCATE(LOWER('a'), LOWER('abc'))",
            read={
                "clickhouse": "positionCaseInsensitive('abc','a')",
            },
        )
        self.validate_all(
            "LOCATE(LOWER('a'), LOWER('abc'))",
            read={
                "clickhouse": "positionCaseInsensitiveUTF8('abc','a')",
            },
        )

        self.validate_all(
            "LOCATE('bar', 'foobarbar', 5)",
            read={
                "clickhouse": "position('foobarbar', 'bar', 5)",
                "spark": "position('bar', 'foobarbar', 5)",
            },
        )
        self.validate_all(
            "LOWER('ABcdEf')",
            read={
                "clickhouse": "lowerUTF8('ABcdEf')",
            },
        )
        self.validate_all(
            "UPPER('ABcdEf')",
            read={
                "clickhouse": "upperUTF8('ABcdEf')",
            },
        )
        self.validate_all(
            "SUBSTRING('ABcdEf', 1, 2)",
            read={
                "clickhouse": "substringUTF8('ABcdEf',1,2)",
            },
        )
        self.validate_all(
            "ENDS_WITH('中国', '国')",
            read={
                "clickhouse": "endsWith('中国', '国')",
            },
        )
        self.validate_all(
            "STARTS_WITH('hello doris', 'hello')",
            read={
                "clickhouse": "startsWith('hello doris', 'hello')",
            },
        )
        self.validate_all(
            "LTRIM('     Hello, world!     ')",
            read={
                "clickhouse": "trimLeft('     Hello, world!     ')",
            },
        )
        self.validate_all(
            "RTRIM('     Hello, world!     ')",
            read={
                "clickhouse": "trimRIGHT('     Hello, world!     ')",
            },
        )
        self.validate_all(
            "TRIM('     Hello, world!     ')",
            read={
                "clickhouse": "trimBOTH('     Hello, world!     ')",
            },
        )
        self.validate_all(
            "LTRIM('xxxbarxxx', 'x')",
            read={
                "oracle": "TRIM(LEADING 'x' FROM 'xxxbarxxx')",
                "postgres": "TRIM(LEADING 'x' FROM 'xxxbarxxx')",
            },
        )
        self.validate_all(
            "RTRIM('barxxyz', 'xyz')",
            read={
                "oracle": "TRIM(TRAILING 'xyz' FROM 'barxxyz')",
                "postgres": "TRIM(TRAILING 'xyz' FROM 'barxxyz')",
            },
        )
        self.validate_all(
            "TRIM('xxxbarxxx', 'x')",
            read={
                "oracle": "TRIM(BOTH 'x' FROM 'xxxbarxxx')",
                "postgres": "TRIM(BOTH 'x' FROM 'xxxbarxxx')",
            },
        )
        self.validate_all(
            "SPLIT_BY_STRING('adidas', 'a')",
            read={
                "clickhouse": "splitByString('a', 'adidas')",
            },
        )
        self.validate_all(
            "MULTI_MATCH_ANY('Hello, World!', ARRAY('hello', '!', 'world'))",
            read={
                "clickhouse": "multiMatchAny('Hello, World!', ['hello', '!', 'world'])",
            },
        )
        self.validate_all(
            "LENGTH('x')",
            read={
                "postgres": "octet_length('x')",
                "oracle": "lengthb('x')",
                "spark": "octet_length('x')",
                "clickhouse": "octet_length('x')",
            },
        )
        self.validate_all(
            "CHAR_LENGTH('x')",
            read={
                "clickhouse": "lengthUTF8('x')",
                "oracle": "length('x')",
            },
        )
        self.validate_all(
            "CONCAT_WS(',', 'abcde', 2, NULL, 22)",
            read={
                "postgres": "concat_ws(',', 'abcde', 2, NULL, 22);",
            },
        )
        self.validate_all(
            "DATE_FORMAT(NOW(), '%d')",
            read={
                "oracle": "to_char(sysdate,'dd')",
            },
        )
        self.validate_all(
            "ROUND(1210.73, 2)",
            read={
                "oracle": "to_char(1210.73, '9999.99')",
                "spark": "round(1210.73, 2)",
                "postgres": "to_char(1210.73, '9999D99')",
            },
        )
        self.validate_all(
            "ROUND(1210.73, 2)",
            read={
                "oracle": "to_char(1210.73, 'fm9999.99')",
                "postgres": "to_char(1210.73, '9999D99S')",
            },
        )
        self.validate_all(
            "ROUND(x, 0)",
            read={
                "spark": "rint(x)",
            },
        )
        self.validate_all(
            "DATE_FORMAT(CURRENT_DATE(), '%Y-%m')",
            read={"presto": "to_char(current_date, 'yyyy-mm')"},
        )
        self.validate_all(
            "DATE_FORMAT(DATE_ADD(CAST(day AS DATE), INTERVAL 1 DAY), '%d') = '01'",
            read={"presto": "to_char(date_add('day', 1, cast(day as date)),'dd') ='01'"},
        )
        self.validate_all(
            "NOT_NULL_OR_EMPTY(x)",
            read={"clickhouse": "IsNotNull(x)"},
        )

    def test_code(self):
        self.validate_all(
            "TO_BASE64('x')",
            read={
                "clickhouse": "base64Encode('x')",
                "spark": "base64('x')",
            },
        )
        self.validate_all(
            "FROM_BASE64('x')",
            read={
                "clickhouse": "base64Decode('x')",
            },
        )
        self.validate_all(
            "LOWER(HEX(10))",
            read={
                "postgres": "to_hex(10)",
            },
        )

    def test_geography(self):
        self.validate_all(
            "ST_ASTEXT(ST_POINT(-122.35, 37.55))",
            read={
                "snowflake": "ST_GEOGRAPHYFROMWKB('POINT(-122.35 37.55)')",
            },
        )

    def test_convert(self):
        self.validate_all("CAST(x AS DECIMAL)", read={"postgres": "x::fixeddecimal"})
        self.validate_all(
            "CAST(x AS BIGINT)",
            read={"clickhouse": "TOINT64(x)", "hive": "BIGINT(x)"},
        )
        self.validate_all(
            "COALESCE(CAST(a AS BIGINT), 0)",
            read={"clickhouse": "TOINT64ORZERO(a)"},
        )
        self.validate_all(
            "CAST(x AS BIGINT)",
            read={"clickhouse": "TOINT64ORNULL(x)"},
        )
        self.validate_all(
            "CAST(x AS DOUBLE)",
            read={"clickhouse": "TOFLOAT64(x)"},
        )
        self.validate_all(
            "COALESCE(CAST(x AS DOUBLE), 0)",
            read={"clickhouse": "TOFLOAT64ORZERO(x)"},
        )
        self.validate_all(
            "CAST(x AS TINYINT)",
            read={
                "clickhouse": "TOINT8(x)",
            },
        )
        self.validate_all(
            "CAST(x AS TINYINT)",
            read={
                "clickhouse": "TOINT8ORNULL(x)",
            },
        )
        self.validate_all(
            "COALESCE(CAST(x AS TINYINT), 0)",
            read={
                "clickhouse": "TOINT8ORZERO(x)",
            },
        )
        self.validate_all(
            "CAST(x AS SMALLINT)",
            read={
                "clickhouse": "TOINT16(x)",
            },
        )
        self.validate_all(
            "CAST(x AS SMALLINT)",
            read={
                "clickhouse": "TOINT16ORNULL(x)",
            },
        )
        self.validate_all(
            "COALESCE(CAST(x AS SMALLINT), 0)",
            read={
                "clickhouse": "TOINT16ORZERO(x)",
            },
        )
        self.validate_all(
            "CAST(x AS INT)",
            read={
                "clickhouse": "TOINT32(x)",
            },
        )
        self.validate_all(
            "CAST(x AS INT)",
            read={
                "clickhouse": "TOINT32ORNULL(x)",
            },
        )
        self.validate_all(
            "COALESCE(CAST(x AS INT), 0)",
            read={
                "clickhouse": "TOINT32ORZERO(x)",
            },
        )
        self.validate_all(
            "CAST(x AS DECIMAL(32, 12))",
            read={
                "clickhouse": "TODECIMAL32(x,12)",
            },
        )
        self.validate_all(
            "CAST(x AS DECIMAL(38, 12))",
            read={
                "clickhouse": "TODECIMAL64(x,12)",
            },
        )
        self.validate_all(
            "CAST(x AS DECIMAL(32, 12))",
            read={
                "clickhouse": "toDecimal32OrNull(x,12)",
            },
        )
        self.validate_all(
            "CAST(x AS DECIMAL(38, 12))",
            read={
                "clickhouse": "toDecimal64OrNull(x,12)",
            },
        )
        self.validate_all(
            "COALESCE(CAST(x AS DECIMAL(32, 12)), 0)",
            read={
                "clickhouse": "toDecimal32OrZero(x,12)",
            },
        )
        self.validate_all(
            "COALESCE(CAST(x AS DECIMAL(38, 12)), 0)",
            read={
                "clickhouse": "toDecimal64OrZero(x,12)",
            },
        )
        self.validate_all(
            "CAST(x AS DATE)",
            read={
                "clickhouse": "toDateOrNull(x)",
            },
        )
        self.validate_all(
            "CAST(x AS DATE)",
            read={
                "clickhouse": "toDate32OrNull(x)",
            },
        )
        self.validate_all(
            "COALESCE(CAST(x AS DATE), '1970-01-01')",
            read={
                "clickhouse": "toDateOrZero(x)",
            },
        )
        self.validate_all(
            "COALESCE(CAST(x AS DATE), 0)",
            read={
                "clickhouse": "toDate32OrZero(x)",
            },
        )
        self.validate_all(
            "CAST(x AS DATETIME)",
            read={
                "clickhouse": "toDateTimeOrNull(x)",
            },
        )
        self.validate_all(
            "CAST(x AS DATETIME)",
            read={
                "clickhouse": "toDateTime64OrNull(x)",
            },
        )
        self.validate_all(
            "COALESCE(CAST(x AS DATETIME), '1970-01-01 00:00:00')",
            read={
                "clickhouse": "toDateTimeOrZero(x)",
            },
        )
        self.validate_all(
            "COALESCE(CAST(x AS DATETIME), '1970-01-01 00:00:00')",
            read={
                "clickhouse": "toDateTime64OrZero(x)",
            },
        )
        self.validate_all(
            "CAST(x AS DATETIME)",
            read={
                "clickhouse": "toDateTime64(x)",
            },
        )

    def test_json(self):
        self.validate_all(
            'JSON_LENGTH(\'{"a": "hello", "b": [-100, 200.0, 300]}\', \'b\') = 3',
            read={
                "clickhouse": 'JSONLength(\'{"a": "hello", "b": [-100, 200.0, 300]}\', \'b\') = 3',
            },
        )
        self.validate_all(
            "COLLECT_LIST(DISTINCT x)",
            read={
                "postgres": "JSON_AGG(distinct x)",
            },
        )
        self.validate_all(
            "JSON_ARRAY(x)",
            read={
                "postgres": "JSON_BUILD_ARRAY(x)",
            },
        )
        self.validate_all(
            "JSONB_EXTRACT('{\"id\": \"33\"}', '$.id')",
            read={
                "clickhouse": "JSONExtractString('{\"id\": \"33\"}' , 'id')",
            },
        )
        self.validate_all(
            "JSONB_EXTRACT('{\"id\": \"33\"}', '$.id')",
            read={
                "clickhouse": "JSONExtractRaw('{\"id\": \"33\"}' , 'id')",
            },
        )
        self.validate_all(
            "JSONB_EXTRACT('{\"id\": \"33\"}', '$.id')",
            read={
                "clickhouse": "JSONExtractInt('{\"id\": \"33\"}' , 'id')",
            },
        )
        self.validate_all(
            "JSONB_EXTRACT('{\"id\": \"33\"}', '$.id.name')",
            read={
                "clickhouse": "JSONExtractString('{\"id\": \"33\"}' , 'id', 'name')",
            },
        )
        self.validate_all(
            'JSONB_EXTRACT(\'{"f2":{"f3":1},"f4":{"f5":99,"f6":"foo"}}\', \'$.f4\')',
            read={
                "postgres": 'json_extract_path(\'{"f2":{"f3":1},"f4":{"f5":99,"f6":"foo"}}\', \'f4\')',
            },
        )
        self.validate_all(
            "JSON_CONTAINS(x, '1')",
            read={
                "mysql": "JSON_ARRAY_CONTAINS(x, '1')",
                "presto": "JSON_ARRAY_CONTAINS(x, 1)",
                "clickhouse": "JSONHas(x, '1')",
            },
        )
        self.validate_all(
            'JSONB_EXTRACT(\'["a", "b", "c"]\', \'$[0]\')',
            read={
                "presto": 'json_array_get(\'["a", "b", "c"]\', 0)',
            },
        )
        self.validate_all(
            "JSON_PARSE(x)",
            read={
                "presto": "JSON_PARSE(x)",
                "snowflake": "PARSE_JSON(x)",
                "bigquery": "PARSE_JSON(x)",
            },
        )
        self.validate_all(
            "JSON_LENGTH(x)",
            read={
                "presto": "JSON_ARRAY_LENGTH(x)",
                "trino": "JSON_ARRAY_LENGTH(x)",
            },
        )
        self.validate_all(
            'JSON_LENGTH(\'{"x": {"a": 1, "b": 2}}\', \'$.x\')',
            read={
                "presto": 'JSON_SIZE(\'{"x": {"a": 1, "b": 2}}\', \'$.x\')',
                "trino": 'JSON_SIZE(\'{"x": {"a": 1, "b": 2}}\', \'$.x\')',
            },
        )

    def test_map(self):
        self.validate_all(
            "MAP_CONTAINS_KEY(map, key)",
            read={
                "clickhouse": "mapContains(map, key)",
            },
        )
        self.validate_all(
            "MAP_KEYS(map)",
            read={
                "clickhouse": "mapKeys(map)",
            },
        )
        self.validate_all(
            "MAP_VALUES(map)",
            read={
                "clickhouse": "mapValues(map)",
            },
        )

    def test_math(self):
        self.validate_all("a + b", read={"clickhouse": "plus(a, b)"})
        self.validate_all("a - b", read={"clickhouse": "minus(a, b)"})
        self.validate_all("a * b", read={"clickhouse": "multiply(a, b)"})
        self.validate_all("a / b", read={"clickhouse": "divide(a, b)"})
        self.validate_all(
            "COALESCE(CAST(a / b AS INT), 0)", read={"clickhouse": "intDivOrZero(a, b)"}
        )
        self.validate_all("COALESCE(a % b, 0)", read={"clickhouse": "moduloOrZero(a, b)"})
        self.validate_all(
            "a % b",
            read={
                "clickhouse": "modulo(a,b)",
            },
        )
        self.validate_all(
            "STDDEV_POP(x)",
            read={
                "clickhouse": "stddevPop(x)",
            },
        )
        self.validate_all(
            "STDDEV_SAMP(x)",
            read={
                "clickhouse": "stddevSamp(x)",
            },
        )
        self.validate_all(
            "VAR_SAMP(x)",
            read={
                "clickhouse": "varSamp(x)",
            },
        )
        self.validate_all(
            "VARIANCE_POP(x)",
            read={
                "clickhouse": "varPop(x)",
            },
        )
        self.validate_all(
            "POWER(2, 3)",
            read={
                "clickhouse": "exp2(3)",
            },
        )
        self.validate_all(
            "POWER(10, 3)",
            read={
                "clickhouse": "EXP10(3)",
            },
        )
        self.validate_all(
            "LOG10(x)",
            read={
                "duckdb": "LOG(x)",
                "postgres": "LOG(x)",
                "redshift": "LOG(x)",
                "sqlite": "LOG(x)",
                "teradata": "LOG(x)",
            },
        )
        self.validate_all(
            "SELECT TRUNCATE(123.458, 1)",
            read={"hive": "select trunc(123.458,1)", "oracle": "select trunc(123.458,1)"},
        )
        self.validate_all(
            "SELECT TRUNCATE(123.458, -1)",
            read={"hive": "select trunc(123.458,-1)", "oracle": "select trunc(123.458,-1)"},
        )
        self.validate_all(
            "TRUNCATE(123)",
            read={
                "postgres": "trunc(123)",
                "hive": "trunc(123)",
                "oracle": "trunc(123)",
            },
        )
        self.validate_all(
            "CAST(a / b AS INT)",
            read={
                "clickhouse": "intDiv(a,b)",
            },
        )

    def test_agg(self):
        self.validate_all(
            "SELECT GROUP_CONCAT(CITY,',' ORDER BY CITY)",
            read={
                "oracle": "SELECT LISTAGG(CITY, ',') WITHIN GROUP (ORDER BY CITY)",
            },
        )
        self.validate_all(
            "GROUP_CONCAT(`base_caseNumber_labelObject`, '|')",
            read={"doris": "GROUP_CONCAT(`base_caseNumber_labelObject`, '|')"},
            write={
                "redshift": "LISTAGG(\"base_caseNumber_labelObject\", '|')",
                "snowflake": "LISTAGG(\"base_caseNumber_labelObject\", '|')",
                "postgres": "STRING_AGG(\"base_caseNumber_labelObject\", '|')",
            },
        )
        self.validate_all(
            "SELECT AVG(x)",
            read={
                "spark": "SELECT mean(x)",
            },
        )
        self.validate_all(
            "HLL_CARDINALITY(HLL_HASH(x))",
            read={
                "clickhouse": "uniqCombined(x)",
            },
        )

    def test_explain(self):
        self.validate_all(
            "explain SELECT * FROM (SELECT id, sum(CASE WHEN a = '2' THEN cost ELSE 0 END) AS avg FROM t GROUP BY id)",
            read={
                "presto": "explain select * from (select id,sum(cost) filter(where a='2') as avg from t group by id)",
            },
        )
        self.validate_all(
            "EXPLAIN SHAPE PLAN SELECT COUNT(*), ANY_VALUE(y) FROM (SELECT COUNT(*) FROM test1)",
            read={
                "presto": "EXPLAIN SHAPE PLAN select count(*),arbitrary(y) from (select count(*) from test1)",
            },
        )
        self.validate_all(
            "EXPLAIN VERBOSE SELECT COUNT(*), ANY_VALUE(y) FROM (SELECT COUNT(*) FROM test1)",
            read={
                "presto": "EXPLAIN VERBOSE select count(*),arbitrary(y) from (select count(*) from test1)",
            },
        )
        self.validate_all(
            "EXPLAIN MEMO PLAN SELECT COUNT(*), ANY_VALUE(y) FROM (SELECT COUNT(*) FROM test1)",
            read={
                "presto": "EXPLAIN MEMO PLAN select count(*),arbitrary(y) from (select count(*) from test1)",
            },
        )
        self.validate_all(
            "EXPLAIN PHYSICAL PLAN SELECT COUNT(*), ANY_VALUE(y) FROM (SELECT COUNT(*) FROM test1)",
            read={
                "presto": "EXPLAIN PHYSICAL PLAN select count(*),arbitrary(y) from (select count(*) from test1)",
            },
        )

    def test_case_sensitive(self):
        import sqlglot
        from sqlglot.optimizer.qualify_tables import qualify_tables

        expected_result_1 = "SELECT * FROM T AS T"
        input_sql_1 = """select * from t"""
        result_1 = qualify_tables(
            sqlglot.parse_one(read="presto", sql=input_sql_1), case_sensitive=True
        ).sql("doris")
        assert (
            result_1 == expected_result_1
        ), f"Transpile result doesn't match expected result. Expected: {expected_result_1}, Actual: {result_1}"
        print("Test1 passed!")

        expected_result_2 = "SELECT * FROM t AS t"
        input_sql_2 = """select * from T"""
        result_2 = qualify_tables(
            sqlglot.parse_one(read="presto", sql=input_sql_2), case_sensitive=False
        ).sql("doris")
        assert (
            result_2 == expected_result_2
        ), f"Transpile result doesn't match expected result. Expected: {expected_result_2}, Actual: {result_2}"
        print("Test2 passed!")

    def test_Quoting(self):
        import sqlglot
        from sqlglot.optimizer.qualify_columns import quote_identifiers

        self.validate_all(
            "SELECT `a` FROM t1",
            read={"presto": 'select "a" from t1', "postgres": "SELECT `a` FROM t1"},
        )
        expected_result_3 = "SELECT `key`, LOWER(`key`), LOWER(t) FROM hive.`default`.tbl"
        input_sql_3 = """select key,lower(key),lower(t) from hive.default.tbl"""
        result_3 = quote_identifiers(
            sqlglot.parse_one(read="hive", sql=input_sql_3), dialect="doris"
        ).sql("doris")
        assert (
            result_3 == expected_result_3
        ), f"Transpile result doesn't match expected result. Expected: {expected_result_3}, Actual: {result_3}"
        print("Test3 passed!")

    def test_mysql2doris_create(self):
        self.validate_all(
            "CREATE TABLE IF NOT EXISTS z (a VARCHAR COMMENT 'pk', b STRING DEFAULT 'aaa' COMMENT 'b')\nUNIQUE KEY(`a`)\nDISTRIBUTED BY HASH(`a`) BUCKETS AUTO\nPROPERTIES (\n    \"replication_allocation\" = \"tag.location.default: 3\"\n)",
            read={
                "mysql": "CREATE TABLE IF NOT EXISTS z (a STRING PRIMARY KEY COMMENT 'pk', b string DEFAULT 'aaa' COMMENT 'b') ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARACTER SET=utf8 COLLATE=utf8_bin COMMENT='x'"
            },
        )

        self.validate_all(
            'CREATE TABLE `x` (`username` VARCHAR(600))\nUNIQUE KEY(`username`)\nDISTRIBUTED BY HASH(`username`) BUCKETS AUTO\nPROPERTIES (\n    "replication_allocation" = "tag.location.default: 3"\n)',
            read={
                "mysql": "CREATE TABLE `x` (`username` VARCHAR(200), PRIMARY KEY (`username`)) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARACTER SET=utf8 COLLATE=utf8_bin COMMENT='x'"
            },
        )

        self.validate_all(
            'CREATE TABLE `x` (`a` INT, `b` VARCHAR, `c` VARCHAR(60))\nUNIQUE KEY(`a`, `b`)\nDISTRIBUTED BY HASH(`a`, `b`) BUCKETS AUTO\nPROPERTIES (\n    "replication_allocation" = "tag.location.default: 3"\n)',
            read={
                "mysql": "CREATE TABLE `x` (`a` INT, `b` string, `c` varchar(20), PRIMARY KEY (`a`, `b`)) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARACTER SET=utf8 COLLATE=utf8_bin COMMENT='x'"
            },
        )

        self.validate_all(
            'CREATE TABLE `x` (`a` INT, `b` VARCHAR, `c` VARCHAR(60))\nUNIQUE KEY(`a`, `b`)\nDISTRIBUTED BY HASH(`a`, `b`) BUCKETS AUTO\nPROPERTIES (\n    "replication_allocation" = "tag.location.default: 3"\n)',
            read={
                "mysql": "CREATE TABLE `x` (`a` INT, `b` string, `c` varchar(20), UNIQUE KEY (`a`, `b`)) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARACTER SET=utf8 COLLATE=utf8_bin COMMENT='x'"
            },
        )

        self.validate_all(
            'CREATE TABLE t1 (a INT NOT NULL, b INT)\nUNIQUE KEY(`a`)\nDISTRIBUTED BY HASH(`a`) BUCKETS AUTO\nPROPERTIES (\n    "replication_allocation" = "tag.location.default: 3"\n)',
            read={
                "mysql": "create table t1 (a int not null, b int, primary key(a), key (b), key (b), key (b), key (b), key (b), key (b), key (b), key (b), key (b), key (b), key (b), key (b), key (b), key (b), key (b), key (b), key (b), key (b), key (b), key (b), key (b), key (b), key (b), key (b), key (b), key (b), key (b), key (b), key (b), key (b), key (b));"
            },
        )

        self.validate_all(
            'CREATE TABLE t1 (`primary` INT)\nDUPLICATE KEY(`primary`)\nDISTRIBUTED BY HASH(`primary`) BUCKETS AUTO\nPROPERTIES (\n    "replication_allocation" = "tag.location.default: 3"\n)',
            read={"mysql": "create table t1 (`primary` int, index(`primary`));"},
        )

        self.validate_all(
            'CREATE TABLE t1 (id VARCHAR(30) NOT NULL, dsc STRING)\nUNIQUE KEY(`id`)\nDISTRIBUTED BY HASH(`id`) BUCKETS AUTO\nPROPERTIES (\n    "replication_allocation" = "tag.location.default: 3"\n)',
            read={
                "mysql": "CREATE TABLE t1(id varchar(10) NOT NULL PRIMARY KEY, dsc longtext) ENGINE=InnoDB AUTO_INCREMENT=1;"
            },
        )

        self.validate_all(
            'CREATE TABLE x (id INT NOT NULL)\nUNIQUE KEY(`id`)\nDISTRIBUTED BY HASH(`id`) BUCKETS AUTO\nPROPERTIES (\n    "replication_allocation" = "tag.location.default: 3"\n)',
            read={
                "mysql": "CREATE TABLE x (id int not null auto_increment PRIMARY KEY, primary key(id))"
            },
        )

        self.validate_all(
            'CREATE TABLE IF NOT EXISTS t2 (a INT NOT NULL)\nUNIQUE KEY(`a`)\nDISTRIBUTED BY HASH(`a`) BUCKETS AUTO\nPROPERTIES (\n    "replication_allocation" = "tag.location.default: 3"\n)',
            read={
                "mysql": "CREATE TABLE IF NOT EXISTS t2 (a INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY)"
            },
        )

        self.validate_all(
            'CREATE TABLE B (pk INT, int_key INT NOT NULL)\nUNIQUE KEY(`pk`)\nDISTRIBUTED BY HASH(`pk`) BUCKETS AUTO\nPROPERTIES (\n    "replication_allocation" = "tag.location.default: 3"\n)',
            read={
                "mysql": "CREATE TABLE B (pk INTEGER AUTO_INCREMENT, int_key INTEGER NOT NULL, PRIMARY KEY (pk), KEY (int_key));"
            },
        )

        self.validate_all(
            'CREATE TABLE t2 (a INT)\nUNIQUE KEY(`a`)\nDISTRIBUTED BY HASH(`a`) BUCKETS AUTO\nPROPERTIES (\n    "replication_allocation" = "tag.location.default: 3"\n)',
            read={"mysql": "create table t2 (a int unique key);"},
        )

        self.validate_all(
            "CREATE TABLE t1 (a INT, b SMALLINT, c INT, d BOOLEAN, e SMALLINT, f INT, "
            "g BIGINT, i DECIMAL(20, 10), j DECIMAL(33, 10), k DATETIME(6), "
            "l SMALLINT, m STRING, n CHAR, o VARCHAR(30), p STRING, q BOOLEAN, "
            "u STRING, v STRING, w STRING, x STRING, y STRING, z STRING, aa STRING, bb STRING, cc STRING, "
            "ff STRING, gg STRING, hh STRING, ii STRING)\n"
            "UNIQUE KEY(`a`)\nDISTRIBUTED BY HASH(`a`) BUCKETS AUTO\nPROPERTIES "
            '(\n    "replication_allocation" = "tag.location.default: 3"\n)',
            read={
                "mysql": "create table t1 (a INT, b SMALLINT, c MEDIUMINT, d BOOLEAN, e TINYINT UNSIGNED, f MEDIUMINT UNSIGNED, "
                "g INT UNSIGNED, i DECIMAL(20, 10), j DECIMAL(32, 10) UNSIGNED, k TIMESTAMP(6), "
                "l YEAR, m TIME, n CHAR, o VARCHAR(10), p SET, q BIT(1),"
                "u TINYTEXT, v TEXT, w MEDIUMTEXT, x LONGTEXT, y BLOB, z MEDIUMBLOB, aa LONGBLOB, bb TINYBLOB, cc STRING, "
                "ff BINARY, gg VARBINARY, hh DECIMAL(38, 10) UNSIGNED, ii BIT(2), PRIMARY KEY (a));"
            },
        )

        self.validate_all(
            'CREATE TABLE t2 (a INT, b BOOLEAN, c DATETIME, d DECIMAL, e DECIMAL)\nDUPLICATE KEY(`a`)\nDISTRIBUTED BY HASH(`a`) BUCKETS AUTO\nPROPERTIES (\n    "replication_allocation" = "tag.location.default: 3"\n)',
            read={
                "mysql": "create table t2 (a int, b bit, c timestamp, d decimal, e decimal UNSIGNED);"
            },
        )

        self.validate_all(
            'CREATE TABLE tb_emp6 (id INT(11), name VARCHAR(75), deptId INT(11), salary FLOAT)\nUNIQUE KEY(`id`)\nDISTRIBUTED BY HASH(`id`) BUCKETS AUTO\nPROPERTIES (\n    "replication_allocation" = "tag.location.default: 3"\n)',
            read={
                "mysql": "CREATE TABLE tb_emp6 (id INT(11) PRIMARY KEY, name VARCHAR(25), deptId INT(11), salary FLOAT, CONSTRAINT fk_emp_dept1 FOREIGN KEY(deptId) REFERENCES tb_dept1(id));"
            },
        )

    def test_clickhouse2doris_create(self):
        self.validate_all(
            'CREATE TABLE kdwtemp.top300song (`songid` VARCHAR, name STRING, `room_cnt` ARRAY<STRUCT<col_1: STRING, col_2: DECIMAL, col_3: INT>>, `max_cnt` INT)\nDUPLICATE KEY(`songid`)\nDISTRIBUTED BY HASH(`songid`) BUCKETS AUTO\nPROPERTIES (\n    "replication_allocation" = "tag.location.default: 3"\n)',
            read={
                "clickhouse": "CREATE TABLE kdwtemp.top300song (`songid` String, name Nullable(String), `room_cnt` Array(Tuple(String, Decimal(32,8), Int32)), `max_cnt` Int32) ENGINE = MergeTree ORDER BY songid SETTINGS index_granularity = 8192;"
            },
        )

        self.validate_all(
            "CREATE TABLE block_chain.bc_playrecord_month_analysis_local (`companycode` BIGINT COMMENT '商家号', `encryptcode` STRING COMMENT '加密商家号', `songid` STRING COMMENT '歌曲id', `playnum` SMALLINT COMMENT '点播次数', `hashdir` STRING COMMENT 'hash地址', `playmonth` DATE COMMENT '日期分区键')\nDUPLICATE KEY(`companycode`)\nDISTRIBUTED BY HASH(`companycode`) BUCKETS AUTO\nPROPERTIES (\n    \"replication_allocation\" = \"tag.location.default: 3\"\n)",
            read={
                "clickhouse": "CREATE TABLE block_chain.bc_playrecord_month_analysis_local (`companycode` int64 COMMENT '商家号', `encryptcode` String COMMENT '加密商家号', `songid` String COMMENT '歌曲id', `playnum` UInt8 COMMENT '点播次数', `hashdir` String COMMENT 'hash地址', `playmonth` Date COMMENT '日期分区键') ENGINE = MergeTree PARTITION BY toYYYYMM(playmonth) ORDER BY (companycode, songid, playmonth) TTL playmonth + toIntervalYear(1) SETTINGS index_granularity = 8192"
            },
        )

        self.validate_all(
            "CREATE TABLE kdwuser.km_tbl_active_user_event_comp_bitmap (`p_ds` DATE COMMENT '快照日期', `event_id` STRING COMMENT '事件id', `company_code` STRING COMMENT '商家编码', `openid_bit` STRING COMMENT '位图数据', `crossopenid_bit` STRING COMMENT 'crosspenid位图数据')\nDUPLICATE KEY(`p_ds`)\nDISTRIBUTED BY HASH(`p_ds`) BUCKETS AUTO\nPROPERTIES (\n    \"replication_allocation\" = \"tag.location.default: 3\"\n)",
            read={
                "clickhouse": "CREATE TABLE kdwuser.km_tbl_active_user_event_comp_bitmap (`p_ds` Date COMMENT '快照日期', `event_id` String COMMENT '事件id', `company_code` String COMMENT '商家编码', `openid_bit` String COMMENT '位图数据', `crossopenid_bit` String COMMENT 'crosspenid位图数据') ENGINE = Distributed('ktvme_ck_cluster', 'kdwuser', 'km_tbl_active_user_event_comp_bitmap_local', rand())"
            },
        )

        self.validate_all(
            'CREATE TABLE hits_UserID_URL (`UserID` BIGINT, `URL` VARCHAR, `EventTime` DATETIME)\nUNIQUE KEY(`UserID`, `URL`)\nDISTRIBUTED BY HASH(`UserID`, `URL`) BUCKETS AUTO\nPROPERTIES (\n    "replication_allocation" = "tag.location.default: 3"\n)',
            read={
                "clickhouse": "CREATE TABLE hits_UserID_URL (`UserID` UInt32, `URL` String, `EventTime` DateTime)ENGINE = MergeTree PRIMARY KEY (UserID, URL) ORDER BY (UserID, URL, EventTime) SETTINGS index_granularity = 8192, index_granularity_bytes = 0"
            },
        )

        self.validate_all(
            'CREATE TABLE hits_UserID_URL (`UserID` BIGINT, `URL` VARCHAR, `EventTime` DATETIME)\nUNIQUE KEY(`UserID`, `URL`)\nDISTRIBUTED BY HASH(`UserID`, `URL`) BUCKETS AUTO\nPROPERTIES (\n    "replication_allocation" = "tag.location.default: 3"\n)',
            read={
                "clickhouse": "CREATE TABLE hits_UserID_URL (`UserID` UInt32, `URL` String, `EventTime` DateTime, PRIMARY KEY (UserID, URL))ENGINE = MergeTree ORDER BY (UserID, URL, EventTime) SETTINGS index_granularity = 8192, index_granularity_bytes = 0"
            },
        )

        self.validate_all(
            'CREATE TABLE test_domain (id INT, ip1 IPV4, ip2 IPV6)\nDUPLICATE KEY(`id`)\nDISTRIBUTED BY HASH(`id`) BUCKETS AUTO\nPROPERTIES (\n    "replication_allocation" = "tag.location.default: 3"\n)',
            read={
                "clickhouse": "create table test_domain(id UInt16, ip1 IPv4, ip2 IPv6) engine = Memory;"
            },
        )

    def test_hive2doris_create(self):
        self.maxDiff = None

        self.validate_all(
            'CREATE TABLE all_data_types_table (id INT, tinyint_column TINYINT)\nDUPLICATE KEY(`id`)\nDISTRIBUTED BY HASH(`id`) BUCKETS AUTO\nPROPERTIES (\n    "replication_allocation" = "tag.location.default: 3"\n)',
            read={
                "hive": "CREATE TABLE all_data_types_table (id INT, tinyint_column TINYINT)",
            },
        )

        self.validate_all(
            'CREATE TABLE all_data_types_table (id INT, tinyint_column TINYINT, smallint_column SMALLINT, bigint_column BIGINT, boolean_column BOOLEAN, float_column FLOAT, double_column DOUBLE, decimal_column DECIMAL(10, 2), string_column STRING, char_column CHAR(30), varchar_column VARCHAR(150), binary_column STRING, timestamp_column DATETIME, date_column DATE, array_column ARRAY<STRING>, map_column MAP<STRING, STRING>, struct_column STRUCT<name:STRING, age:INT>)\nDUPLICATE KEY(`id`)\nDISTRIBUTED BY HASH(`id`) BUCKETS AUTO\nPROPERTIES (\n    "replication_allocation" = "tag.location.default: 3"\n)',
            read={
                "hive": "CREATE TABLE all_data_types_table (id INT, tinyint_column TINYINT, smallint_column SMALLINT, bigint_column BIGINT, boolean_column BOOLEAN, float_column FLOAT, double_column DOUBLE, decimal_column DECIMAL(10, 2), string_column STRING, char_column CHAR(10), varchar_column VARCHAR(50), binary_column BINARY, timestamp_column TIMESTAMP, date_column DATE, array_column ARRAY<STRING>, map_column MAP<STRING, STRING>, struct_column STRUCT<name:STRING, age:INT>)",
            },
        )

        self.validate_all(
            'CREATE TABLE all_data_types_table (id INT, tinyint_column TINYINT, smallint_column SMALLINT, bigint_column BIGINT, boolean_column BOOLEAN, float_column FLOAT, double_column DOUBLE, decimal_column DECIMAL(10, 2), string_column STRING, char_column CHAR(30), varchar_column VARCHAR(150), binary_column STRING, timestamp_column DATETIME, date_column DATE, array_column ARRAY<STRING>, map_column MAP<STRING, STRING>, struct_column STRUCT<name:STRING, age:INT>)\nDUPLICATE KEY(`id`)\nDISTRIBUTED BY HASH(`id`) BUCKETS AUTO\nPROPERTIES (\n    "replication_allocation" = "tag.location.default: 3"\n)',
            read={
                "hive": "CREATE TABLE all_data_types_table (id INT, tinyint_column TINYINT, smallint_column SMALLINT, bigint_column BIGINT, boolean_column BOOLEAN, float_column FLOAT, double_column DOUBLE, decimal_column DECIMAL(10, 2), string_column STRING, char_column CHAR(10), varchar_column VARCHAR(50), binary_column BINARY, timestamp_column TIMESTAMP, date_column DATE, array_column ARRAY<STRING>, map_column MAP<STRING, STRING>, struct_column STRUCT<name:STRING, age:INT>) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n' STORED AS TEXTFILE",
            },
        )

        self.validate_all(
            'CREATE TABLE all_data_types_table (id INT NOT NULL, day DATE NOT NULL)\nDUPLICATE KEY(`id`)\nAUTO PARTITION BY RANGE date_trunc(`day`, \'day\') ()\nDISTRIBUTED BY HASH(`id`) BUCKETS AUTO\nPROPERTIES (\n    "replication_allocation" = "tag.location.default: 3"\n)',
            read={
                "hive": "CREATE TABLE all_data_types_table (id INT NOT NULL) PARTITIONED BY (day DATE) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n' STORED AS TEXTFILE",
            },
        )

        self.validate_all(
            'CREATE TABLE all_data_types_table (id INT NOT NULL, tinyint_column TINYINT, smallint_column SMALLINT, bigint_column BIGINT, boolean_column BOOLEAN, float_column FLOAT, double_column DOUBLE, decimal_column DECIMAL(10, 2), string_column STRING, char_column CHAR(30), varchar_column VARCHAR(150), binary_column STRING, timestamp_column DATETIME, date_column DATE, array_column ARRAY<STRING>, map_column MAP<STRING, STRING>, struct_column STRUCT<name:STRING, age:INT>, date STRING, day DATE NOT NULL)\nDUPLICATE KEY(`id`)\nAUTO PARTITION BY RANGE date_trunc(`day`, \'day\') ()\nDISTRIBUTED BY HASH(`id`) BUCKETS AUTO\nPROPERTIES (\n    "replication_allocation" = "tag.location.default: 3"\n)',
            read={
                "hive": "CREATE TABLE all_data_types_table (id INT NOT NULL, tinyint_column TINYINT, smallint_column SMALLINT, bigint_column BIGINT, boolean_column BOOLEAN, float_column FLOAT, double_column DOUBLE, decimal_column DECIMAL(10, 2), string_column STRING, char_column CHAR(10), varchar_column VARCHAR(50), binary_column BINARY, timestamp_column TIMESTAMP, date_column DATE, array_column ARRAY<STRING>, map_column MAP<STRING, STRING>, struct_column STRUCT<name:STRING, age:INT>) PARTITIONED BY (date STRING, day DATE) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n' LOCATION '/data/tmp/external_table/' STORED AS TEXTFILE",
            },
        )

        self.validate_all(
            'CREATE TABLE all_data_types_table (id INT NOT NULL, tinyint_column TINYINT, smallint_column SMALLINT, bigint_column BIGINT, boolean_column BOOLEAN, float_column FLOAT, double_column DOUBLE, decimal_column DECIMAL(10, 2), string_column STRING, char_column CHAR(30), varchar_column VARCHAR(150), binary_column STRING, timestamp_column DATETIME, date_column DATE, array_column ARRAY<STRING>, map_column MAP<STRING, STRING>, struct_column STRUCT<name:STRING, age:INT>)\nDUPLICATE KEY(`id`)\nDISTRIBUTED BY HASH(`id`, `tinyint_column`) BUCKETS AUTO\nPROPERTIES (\n    "replication_allocation" = "tag.location.default: 3"\n)',
            read={
                "hive": "CREATE TABLE all_data_types_table (id INT NOT NULL, tinyint_column TINYINT, smallint_column SMALLINT, bigint_column BIGINT, boolean_column BOOLEAN, float_column FLOAT, double_column DOUBLE, decimal_column DECIMAL(10, 2), string_column STRING, char_column CHAR(10), varchar_column VARCHAR(50), binary_column BINARY, timestamp_column TIMESTAMP, date_column DATE, array_column ARRAY<STRING>, map_column MAP<STRING, STRING>, struct_column STRUCT<name:STRING, age:INT>) CLUSTERED BY (id, tinyint_column) SORTED BY (id DESC) INTO 32 BUCKETS ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n' LOCATION '/data/tmp/external_table/' STORED AS TEXTFILE",
            },
        )

        self.validate_all(
            'CREATE TABLE all_data_types_table (id INT NOT NULL, tinyint_column TINYINT, smallint_column SMALLINT, bigint_column BIGINT, boolean_column BOOLEAN, float_column FLOAT, double_column DOUBLE, decimal_column DECIMAL(10, 2), string_column STRING, char_column CHAR(30), varchar_column VARCHAR(150), binary_column STRING, timestamp_column DATETIME, date_column DATE, array_column ARRAY<STRING>, map_column MAP<STRING, STRING>, struct_column STRUCT<name:STRING, age:INT>, date STRING, day DATE NOT NULL)\nDUPLICATE KEY(`id`)\nAUTO PARTITION BY RANGE date_trunc(`day`, \'day\') ()\nDISTRIBUTED BY HASH(`id`, `tinyint_column`) BUCKETS AUTO\nPROPERTIES (\n    "replication_allocation" = "tag.location.default: 3"\n)',
            read={
                "hive": "CREATE TABLE all_data_types_table (id INT NOT NULL, tinyint_column TINYINT, smallint_column SMALLINT, bigint_column BIGINT, boolean_column BOOLEAN, float_column FLOAT, double_column DOUBLE, decimal_column DECIMAL(10, 2), string_column STRING, char_column CHAR(10), varchar_column VARCHAR(50), binary_column BINARY, timestamp_column TIMESTAMP, date_column DATE, array_column ARRAY<STRING>, map_column MAP<STRING, STRING>, struct_column STRUCT<name:STRING, age:INT>) PARTITIONED BY (date STRING, day DATE) CLUSTERED BY (id, tinyint_column) SORTED BY (id DESC) INTO 32 BUCKETS ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n' LOCATION '/data/tmp/external_table/' STORED AS TEXTFILE",
            },
        )

        self.validate_all(
            'CREATE TABLE all_data_types_table (id INT NOT NULL, tinyint_column TINYINT, smallint_column SMALLINT, bigint_column BIGINT, boolean_column BOOLEAN, float_column FLOAT, double_column DOUBLE, decimal_column DECIMAL(10, 2), string_column STRING, char_column CHAR(30), varchar_column VARCHAR(150), binary_column STRING, timestamp_column DATETIME, date_column DATE, array_column ARRAY<STRING>, map_column MAP<STRING, STRING>, struct_column STRUCT<name:STRING, age:INT>, date STRING, day DATE NOT NULL)\nDUPLICATE KEY(`id`)\nAUTO PARTITION BY RANGE date_trunc(`day`, \'day\') ()\nDISTRIBUTED BY HASH(`id`, `tinyint_column`) BUCKETS AUTO\nPROPERTIES (\n    "replication_allocation" = "tag.location.default: 3"\n)',
            read={
                "hive": "CREATE TABLE all_data_types_table (id INT NOT NULL, tinyint_column TINYINT, smallint_column SMALLINT, bigint_column BIGINT, boolean_column BOOLEAN, float_column FLOAT, double_column DOUBLE, decimal_column DECIMAL(10, 2), string_column STRING, char_column CHAR(10), varchar_column VARCHAR(50), binary_column BINARY, timestamp_column TIMESTAMP, date_column DATE, array_column ARRAY<STRING>, map_column MAP<STRING, STRING>, struct_column STRUCT<name:STRING, age:INT>) PARTITIONED BY (date STRING, day DATE) CLUSTERED BY (id, tinyint_column) SORTED BY (id DESC) INTO 32 BUCKETS ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n' LOCATION '/data/tmp/external_table/' STORED AS TEXTFILE",
            },
        )

    def test_presto2doris_create(self):
        self.maxDiff = None
        self.validate_all(
            'CREATE TABLE example_table (id INT, name BOOLEAN, col_tinyint TINYINT, col_date DATE NOT NULL)\nDUPLICATE KEY(`id`)\nAUTO PARTITION BY RANGE date_trunc(`col_date`, \'day\') ()\nDISTRIBUTED BY HASH(`id`, `name`) BUCKETS AUTO\nPROPERTIES (\n    "replication_allocation" = "tag.location.default: 3"\n)',
            read={
                "presto": "CREATE TABLE example_table (id INTEGER, name BOOLEAN, col_tinyint TINYINT, col_date DATE) WITH (format = 'ORC', partitioned_by = ARRAY['col_date'], bucketed_by = ARRAY['id','name'], bucket_count = 16, sorted_by = ARRAY['col_tinyint'])",
            },
        )

        self.validate_all(
            'CREATE TABLE example_table (id INT, name BOOLEAN, col_tinyint TINYINT, col_smallint SMALLINT, col_bigint BIGINT, col_real FLOAT, col_double DOUBLE, col_decimal DECIMAL(10, 5), col_varchar VARCHAR, col_varchar_fixed VARCHAR(300), col_char CHAR(30), col_text STRING, col_binary STRING, col_date DATE NOT NULL, col_time STRING, col_time_with_timezone STRING, col_timestamp DATETIME, col_timestamp_with_timezone DATETIME, col_interval_day_to_second STRING, col_array ARRAY<INT>, col_map MAP<VARCHAR, INT>, col_row STRUCT<nested_col_integer:INT, nested_col_double:DOUBLE>, col_json JSON, col_ipaddress STRING, col_uuid STRING, col_geometry STRING)\nDUPLICATE KEY(`id`)\nAUTO PARTITION BY RANGE date_trunc(`col_date`, \'day\') ()\nDISTRIBUTED BY HASH(`id`) BUCKETS AUTO\nPROPERTIES (\n    "replication_allocation" = "tag.location.default: 3"\n)',
            read={
                "presto": "CREATE TABLE example_table (id INTEGER, name BOOLEAN, col_tinyint TINYINT, col_smallint SMALLINT, col_bigint BIGINT, col_real REAL, col_double DOUBLE, col_decimal DECIMAL(10,5), col_varchar VARCHAR, col_varchar_fixed VARCHAR(100), col_char CHAR(10), col_text TEXT, col_binary VARBINARY, col_date DATE, col_time TIME, col_time_with_timezone TIME WITH TIME ZONE, col_timestamp TIMESTAMP, col_timestamp_with_timezone TIMESTAMP WITH TIME ZONE, col_interval_day_to_second INTERVAL DAY TO SECOND, col_array ARRAY<INTEGER>, col_map MAP<VARCHAR, INTEGER>, col_row STRUCT(nested_col_integer INTEGER, nested_col_double DOUBLE), col_json JSON, col_ipaddress IPADDRESS, col_uuid UUID, col_geometry GEOMETRY) WITH (format = 'ORC', partitioned_by = ARRAY['col_date'], sorted_by = ARRAY['col_tinyint'])",
            },
        )

        self.validate_all(
            'CREATE TABLE example_table (id INT, name BOOLEAN, col_tinyint TINYINT, col_smallint SMALLINT, col_bigint BIGINT, col_real FLOAT, col_double DOUBLE, col_decimal DECIMAL(10, 5), col_varchar VARCHAR, col_varchar_fixed VARCHAR(300), col_char CHAR(30), col_text STRING, col_binary STRING, col_date DATE, col_time STRING, col_time_with_timezone STRING, col_timestamp DATETIME, col_timestamp_with_timezone DATETIME, col_interval_day_to_second STRING, col_array ARRAY<INT>, col_map MAP<VARCHAR, INT>, col_row STRUCT<nested_col_integer:INT, nested_col_double:DOUBLE>, col_json JSON, col_ipaddress STRING, col_uuid STRING, col_geometry STRING)\nDUPLICATE KEY(`id`)\nDISTRIBUTED BY HASH(`id`, `name`) BUCKETS AUTO\nPROPERTIES (\n    "replication_allocation" = "tag.location.default: 3"\n)',
            read={
                "presto": "CREATE TABLE example_table (id INTEGER, name BOOLEAN, col_tinyint TINYINT, col_smallint SMALLINT, col_bigint BIGINT, col_real REAL, col_double DOUBLE, col_decimal DECIMAL(10,5), col_varchar VARCHAR, col_varchar_fixed VARCHAR(100), col_char CHAR(10), col_text TEXT, col_binary VARBINARY, col_date DATE, col_time TIME, col_time_with_timezone TIME WITH TIME ZONE, col_timestamp TIMESTAMP, col_timestamp_with_timezone TIMESTAMP WITH TIME ZONE, col_interval_day_to_second INTERVAL DAY TO SECOND, col_array ARRAY<INTEGER>, col_map MAP<VARCHAR, INTEGER>, col_row STRUCT(nested_col_integer INTEGER, nested_col_double DOUBLE), col_json JSON, col_ipaddress IPADDRESS, col_uuid UUID, col_geometry GEOMETRY) WITH (format = 'ORC', bucketed_by = ARRAY['id','name'], bucket_count = 16, sorted_by = ARRAY['col_tinyint'])",
            },
        )

        self.validate_all(
            'CREATE TABLE example_table (id INT, col_boolean BOOLEAN, col_tinyint TINYINT, col_smallint SMALLINT, col_bigint BIGINT, col_real FLOAT, col_double DOUBLE, col_decimal DECIMAL(10, 5), col_varchar VARCHAR, col_varchar_fixed VARCHAR(300), col_char CHAR(30), col_text STRING, col_binary STRING, col_date DATE, col_time STRING, col_time_with_timezone STRING, col_timestamp DATETIME, col_timestamp_with_timezone DATETIME, col_interval_day_to_second STRING, col_array ARRAY<INT>, col_map MAP<VARCHAR, INT>, col_row STRUCT<nested_col_integer:INT, nested_col_double:DOUBLE>, col_json JSON, col_ipaddress STRING, col_uuid STRING, col_geometry STRING)\nDUPLICATE KEY(`id`)\nDISTRIBUTED BY HASH(`id`) BUCKETS AUTO\nPROPERTIES (\n    "replication_allocation" = "tag.location.default: 3"\n)',
            read={
                "presto": "CREATE TABLE example_table (id INTEGER, col_boolean BOOLEAN, col_tinyint TINYINT, col_smallint SMALLINT, col_bigint BIGINT, col_real REAL, col_double DOUBLE, col_decimal DECIMAL(10, 5), col_varchar VARCHAR, col_varchar_fixed VARCHAR(100), col_char CHAR(10), col_text TEXT, col_binary VARBINARY, col_date DATE, col_time TIME, col_time_with_timezone TIME WITH TIME ZONE, col_timestamp TIMESTAMP, col_timestamp_with_timezone TIMESTAMP WITH TIME ZONE, col_interval_day_to_second INTERVAL DAY TO SECOND, col_array ARRAY<INTEGER>, col_map MAP<VARCHAR, INTEGER>, col_row STRUCT(nested_col_integer INTEGER, nested_col_double DOUBLE), col_json JSON, col_ipaddress IPADDRESS, col_uuid UUID, col_geometry GEOMETRY) WITH (format = 'ORC', comment = 'Example table', read_repair_chance = 0.2, compaction = JSON {\"class\": \"LeveledCompactionStrategy\"})",
            },
        )

        self.validate_all(
            'CREATE TABLE example_table (id INT, col_time_with_timezone STRING)\nDUPLICATE KEY(`id`)\nDISTRIBUTED BY HASH(`id`) BUCKETS AUTO\nPROPERTIES (\n    "replication_allocation" = "tag.location.default: 3"\n)',
            read={
                "presto": "CREATE TABLE example_table (id INTEGER, col_time_with_timezone TIME WITH TIME ZONE) WITH (kafka_topic = 'your_kafka_topic', kafka_broker_list = 'broker1:port,broker2:port', kafka_value_format = 'json')",
            },
        )

    def test_oracle2doris_create(self):
        self.validate_all(
            "CREATE TABLE new_employees LIKE employees",
            read={
                "oracle": "CREATE TABLE new_employees like employees;",
            },
        )

        self.validate_all(
            "CREATE TABLE dept_80 AS SELECT * FROM employees WHERE department_id = 80",
            read={
                "oracle": "CREATE TABLE dept_80 AS SELECT * FROM employees WHERE department_id = 80;",
            },
        )

        self.validate_all(
            "CREATE TABLE emp (id DECIMAL(6), name VARCHAR(75) DEFAULT '1', dept_id DECIMAL(4), name2 VARCHAR(75) DEFAULT '1', sal DECIMAL(8, 2))\nUNIQUE KEY(`id`, `name`, `dept_id`)\nDISTRIBUTED BY HASH(`id`, `name`, `dept_id`) BUCKETS AUTO\nPROPERTIES (\n    \"replication_allocation\" = \"tag.location.default: 3\"\n)",
            read={
                "oracle": "CREATE TABLE emp(id NUMBER(6) PRIMARY KEY, name VARCHAR2(25) DEFAULT 1 UNIQUE, name2 VARCHAR2(25) DEFAULT '1', sal NUMBER(8,2) CHECK(sal > 0 and sal < 1000000), dept_id number(4), constraint dept_fk foreign key(dept_id) REFERENCES dept(dept_id) on delete set null, UNIQUE(dept_id))",
            },
        )

        self.validate_all(
            'CREATE TABLE customers (customer_id DECIMAL(10) NOT NULL, customer_name DECIMAL NOT NULL, city VARCHAR(150))\nUNIQUE KEY(`customer_id`, `customer_name`)\nDISTRIBUTED BY HASH(`customer_id`, `customer_name`) BUCKETS AUTO\nPROPERTIES (\n    "replication_allocation" = "tag.location.default: 3"\n)',
            read={
                "oracle": "CREATE TABLE customers (customer_id number(10) CONSTRAINT customer_id_nn NOT NULL ENABLE, customer_name float NOT NULL, city varchar2(50), CONSTRAINT customers_pk PRIMARY KEY (customer_id, customer_name))",
            },
        )

        self.validate_all(
            'CREATE TABLE customers (customer_id DECIMAL(10) NOT NULL, customer_name DECIMAL, city VARCHAR(150))\nUNIQUE KEY(`customer_id`, `customer_name`)\nDISTRIBUTED BY HASH(`customer_id`, `customer_name`) BUCKETS AUTO\nPROPERTIES (\n    "replication_allocation" = "tag.location.default: 3"\n)',
            read={
                "oracle": "CREATE TABLE customers (customer_id number(10) CONSTRAINT customer_id_nn NOT NULL, customer_name float NOT NULL DISABLE, city varchar2(50), CONSTRAINT customers_pk PRIMARY KEY (customer_id, customer_name))",
            },
        )

        self.validate_all(
            'CREATE TABLE customers (customer_id DECIMAL(10), customer_name DECIMAL NOT NULL, city VARCHAR(150))\nUNIQUE KEY(`customer_id`, `customer_name`)\nDISTRIBUTED BY HASH(`customer_id`, `customer_name`) BUCKETS AUTO\nPROPERTIES (\n    "replication_allocation" = "tag.location.default: 3"\n)',
            read={
                "oracle": "CREATE TABLE customers (customer_id number(10) CONSTRAINT customer_id_nn NOT NULL DISABLE, customer_name float NOT NULL, city varchar2(50), CONSTRAINT customers_pk PRIMARY KEY (customer_id, customer_name))",
            },
        )

        self.validate_all(
            'CREATE TABLE departments_demo (department_id DECIMAL(4), department_name VARCHAR(90) NOT NULL, manager_id DECIMAL(6), location_id DECIMAL(4), dn VARCHAR(900))\nUNIQUE KEY(`department_id`)\nDISTRIBUTED BY HASH(`department_id`) BUCKETS AUTO\nPROPERTIES (\n    "replication_allocation" = "tag.location.default: 3"\n)',
            read={
                "oracle": "CREATE TABLE departments_demo(department_id NUMBER(4) PRIMARY KEY, department_name VARCHAR2(30) CONSTRAINT dept_name_nn NOT NULL, manager_id NUMBER(6), location_id NUMBER(4), dn VARCHAR2(300));",
            },
        )

        self.validate_all(
            'CREATE TABLE employees_demo (email VARCHAR(75) NOT NULL, employee_id DECIMAL(6), first_name VARCHAR(60), last_name VARCHAR(75) NOT NULL, phone_number VARCHAR(60), hire_date DATETIME NOT NULL, job_id VARCHAR(30) NOT NULL, salary DECIMAL(8, 2) NOT NULL, commission_pct DECIMAL(2, 2), manager_id DECIMAL(6), department_id DECIMAL(4), dn VARCHAR(900))\nUNIQUE KEY(`email`)\nDISTRIBUTED BY HASH(`email`) BUCKETS AUTO\nPROPERTIES (\n    "replication_allocation" = "tag.location.default: 3"\n)',
            read={
                "oracle": "CREATE TABLE employees_demo(employee_id NUMBER(6), first_name VARCHAR2(20), last_name VARCHAR2(25) CONSTRAINT emp_last_name_nn NOT NULL, email VARCHAR2(25) CONSTRAINT emp_email_nn NOT NULL, phone_number VARCHAR2(20), hire_date DATE DEFAULT SYSDATE CONSTRAINT emp_hire_date_nn NOT NULL, job_id VARCHAR2(10) CONSTRAINT emp_job_nn NOT NULL, salary NUMBER(8,2) CONSTRAINT emp_salary_nn NOT NULL, commission_pct NUMBER(2,2), manager_id NUMBER(6), department_id NUMBER(4), dn VARCHAR2(300), CONSTRAINT emp_salary_min CHECK (salary > 0), CONSTRAINT emp_email_uk UNIQUE (email))",
            },
        )

        self.validate_all(
            'CREATE TABLE print_media (product_id DECIMAL(6), ad_id DECIMAL(6), pt DATETIME, ad_composite STRING, ad_sourcetext STRING, ad_finaltext STRING, ad_fltextn STRING, ad_photo STRING)\nDUPLICATE KEY(`product_id`)\nDISTRIBUTED BY HASH(`product_id`) BUCKETS AUTO\nPROPERTIES (\n    "replication_allocation" = "tag.location.default: 3"\n)',
            read={
                "oracle": "CREATE TABLE print_media(product_id NUMBER(6), ad_id NUMBER(6), pt date, ad_composite BLOB, ad_sourcetext CLOB, ad_finaltext CLOB, ad_fltextn NCLOB, ad_photo BLOB)",
            },
        )

    def test_ddl(self):
        self.validate_identity(
            'CREATE TABLE hits_UserID_URL (UserID BIGINT, URL VARCHAR, `EventTime` DATETIME) DUPLICATE KEY(UserID, URL) DISTRIBUTED BY HASH(`UserID`) BUCKETS AUTO PROPERTIES ("replication_allocation" = "tag.location.default: 3", "dynamic_partition.enable" = "true", "dynamic_partition.time_unit" = "day", "dynamic_partition.prefix" = "p", "dynamic_partition.end" = "3")',
            "CREATE TABLE hits_UserID_URL (UserID BIGINT, URL VARCHAR, `EventTime` DATETIME) DUPLICATE KEY (UserID, URL) DISTRIBUTED BY HASH (`UserID`) BUCKETS AUTO PROPERTIES ('replication_allocation'='tag.location.default: 3', 'dynamic_partition.enable'='true', 'dynamic_partition.time_unit'='day', 'dynamic_partition.prefix'='p', 'dynamic_partition.end'='3')",
        )

        self.validate_identity(
            'CREATE TABLE hits_UserID_URL (`UserID` BIGINT, `URL` VARCHAR, `EventTime` DATETIME) DUPLICATE KEY(`UserID`, `URL`) DISTRIBUTED BY HASH(`UserID`) BUCKETS AUTO PROPERTIES ("replication_allocation" = "tag.location.default: 3")',
            "CREATE TABLE hits_UserID_URL (`UserID` BIGINT, `URL` VARCHAR, `EventTime` DATETIME) DUPLICATE KEY (`UserID`, `URL`) DISTRIBUTED BY HASH (`UserID`) BUCKETS AUTO PROPERTIES ('replication_allocation'='tag.location.default: 3')",
        )

        self.validate_identity(
            'CREATE TABLE hits_UserID_URL (`UserID` BIGINT, `URL` VARCHAR, `EventTime` DATETIME) UNIQUE KEY(`UserID`, `URL`) DISTRIBUTED BY HASH(`UserID`) BUCKETS AUTO PROPERTIES ("replication_allocation" = "tag.location.default: 3", "dynamic_partition.enable" = "true", "dynamic_partition.time_unit" = "day", "dynamic_partition.prefix" = "p", "dynamic_partition.end" = "3")',
            "CREATE TABLE hits_UserID_URL (`UserID` BIGINT, `URL` VARCHAR, `EventTime` DATETIME) UNIQUE KEY (`UserID`, `URL`) DISTRIBUTED BY HASH (`UserID`) BUCKETS AUTO PROPERTIES ('replication_allocation'='tag.location.default: 3', 'dynamic_partition.enable'='true', 'dynamic_partition.time_unit'='day', 'dynamic_partition.prefix'='p', 'dynamic_partition.end'='3')",
        )

    def test_postgres2doris_create(self):
        self.maxDiff = None
        self.validate_all(
            'CREATE TABLE users (user_id INT, username VARCHAR(150), email VARCHAR(600), created_at DATETIME NOT NULL)\nUNIQUE KEY(`user_id`, `username`, `email`)\nAUTO PARTITION BY RANGE date_trunc(`created_at`, \'day\') ()\nDISTRIBUTED BY HASH(`user_id`, `username`, `email`) BUCKETS AUTO\nPROPERTIES (\n    "replication_allocation" = "tag.location.default: 3"\n)',
            read={
                "postgres": "CREATE TABLE users (user_id SERIAL PRIMARY KEY, username VARCHAR(50) PRIMARY KEY, email VARCHAR(200) UNIQUE, created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP) PARTITION BY RANGE (created_at)",
            },
        )

        self.validate_all(
            'CREATE TABLE users (user_id INT, username VARCHAR(150), email VARCHAR(600), created_at DATETIME NOT NULL)\nUNIQUE KEY(`user_id`, `username`, `email`)\nDISTRIBUTED BY HASH(`user_id`, `username`, `email`) BUCKETS AUTO\nPROPERTIES (\n    "replication_allocation" = "tag.location.default: 3"\n)',
            read={
                "postgres": "CREATE TABLE users (user_id SERIAL PRIMARY KEY, username VARCHAR(50) PRIMARY KEY, email VARCHAR(200) UNIQUE, created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)",
            },
        )

        self.validate_all(
            'CREATE TABLE users (email VARCHAR(600), user_id INT, username VARCHAR(150), created_at DATETIME NOT NULL)\nUNIQUE KEY(`email`)\nAUTO PARTITION BY RANGE date_trunc(`created_at`, \'day\') ()\nDISTRIBUTED BY HASH(`email`) BUCKETS AUTO\nPROPERTIES (\n    "replication_allocation" = "tag.location.default: 3"\n)',
            read={
                "postgres": "CREATE TABLE users (user_id SERIAL, username VARCHAR(50), email VARCHAR(200) UNIQUE, created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP) PARTITION BY RANGE (created_at)",
            },
        )

        self.validate_all(
            'CREATE TABLE users (email VARCHAR(600), user_id INT, username VARCHAR(150), created_at DATETIME NOT NULL)\nUNIQUE KEY(`email`)\nDISTRIBUTED BY HASH(`email`) BUCKETS AUTO\nPROPERTIES (\n    "replication_allocation" = "tag.location.default: 3"\n)',
            read={
                "postgres": "CREATE TABLE users (user_id SERIAL, username VARCHAR(50), email VARCHAR(200) UNIQUE, created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)",
            },
        )

        self.validate_all(
            'CREATE TABLE users (user_id INT, username VARCHAR(150), email VARCHAR(600), created_at DATETIME NOT NULL)\nDUPLICATE KEY(`user_id`)\nDISTRIBUTED BY HASH(`user_id`) BUCKETS AUTO\nPROPERTIES (\n    "replication_allocation" = "tag.location.default: 3"\n)',
            read={
                "postgres": "CREATE TABLE users (user_id SERIAL, username VARCHAR(50), email VARCHAR(200), created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)",
            },
        )

        self.validate_all(
            'CREATE TABLE my_data_types_example (smallint_column SMALLINT, integer_column INT, bigint_column BIGINT, decimal_column DECIMAL(10, 2), numeric_column DECIMAL(14, 4), real_column FLOAT, double_column DOUBLE, money_column STRING, char_column CHAR(30), varchar_column VARCHAR(600), text_column STRING, bytea_column STRING, timestamp_column DATETIME, timestamptz_column DATETIME, date_column DATE, time_column STRING, timetz_column STRING, interval_column STRING, boolean_column BOOLEAN, point_column STRING, line_column STRING, lseg_column STRING, box_column STRING, path_column STRING, polygon_column STRING, circle_column STRING, cidr_column STRING, inet_column STRING, macaddr_column STRING, bit_column STRING, integer_array_column ARRAY<INT>, text_array_column ARRAY<STRING>, enum_type_column STRING, json_column JSON, jsonb_column JSONB, tsvector_column STRING, uuid_column STRING, xml_column STRING)\nDUPLICATE KEY(`smallint_column`)\nDISTRIBUTED BY HASH(`smallint_column`) BUCKETS AUTO\nPROPERTIES (\n    "replication_allocation" = "tag.location.default: 3"\n)',
            read={
                "postgres": "CREATE TABLE my_data_types_example (smallint_column smallint, integer_column integer, bigint_column bigint, decimal_column decimal(10, 2), numeric_column numeric(14, 4), real_column real, double_column double precision, money_column money, char_column char(10), varchar_column varchar(200), text_column text, bytea_column bytea, timestamp_column timestamp without time zone, timestamptz_column timestamp with time zone, date_column date, time_column time without time zone, timetz_column time with time zone, interval_column interval, boolean_column boolean, point_column point, line_column line, lseg_column lseg, box_column box, path_column path, polygon_column polygon, circle_column circle, cidr_column cidr, inet_column inet, macaddr_column macaddr, bit_column bit(5), integer_array_column integer[], text_array_column text[], enum_type_column my_enum_type, json_column json, jsonb_column jsonb, tsvector_column tsvector, uuid_column uuid, xml_column xml)",
            },
        )
