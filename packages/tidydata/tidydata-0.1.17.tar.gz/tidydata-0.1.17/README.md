

## Table对象VS. Pandas DataFrame

1. 每个Table必有一个字符串的name属性;
2. 每个Table有一个字符串可选的description属性，用于描述Table自身
3. 每个Table的行索引总是为默认的RangeIndex;
4. 每个Table的列索引将总是字符串且独一无二且单层,且不为缺失值;
5. 每个Table的列索引将具有额外标签column_labels用于描述列索引;
6. 每个Table的类型转换系统将是简化后的Nullable数据类型;
7. 每个Table的HTML显示，会显示列的简化类型

## MultiTable VS. DiskCache

1. 每个MultiTable的值总是Table对象
2. 每个MultiTable的size_limit将为当前磁盘的free disk_usage*0.95 以及cull_limit将为0;
3. 每个MultiTable的with语句退出后不仅close cache数据库还删除数据库;
4. 增加concat, reshape, eval, aggregate, format操作五个数据pipeline方法:
   1. concat: 横向/纵向合并 （不新增值但改变维度）
   2. reshape: 长转宽/宽转长 （改变形状和行列值）
   3. mutate: 基于现有列计算新列; （根据已有列修改列但不改变维度）
   4. aggregate: 加总列信息为更小行数的列; (根据已有列，创建新Table) （比如从个体加总成家庭层面）
   5. format: 列排序/行排序/表名/表描述/列值范围/列值替换/列数据类型/列名重命名/列名标签 （不改变行列值和形状）
   
5. 区分add和update方法: add仅仅在key不存在时使用, update则将可以更新存在的key; 使用选项来设置是否lock source
6. 通过构造表达式来
   
7. 增加IO：
   1. from_csv
   2. from_tsv
   3. from_pickle
   4. from_stata
   5. to_csv
   6. to_tsv
   7. to_pickle
   8. to_stata