def find_position_of_tenant_id_in_sql(sql_query):
    start = sql_query.find("(") + 1
    end = sql_query.find(")")
    parameters = sql_query[start:end]

    parameter_list = parameters.split(", ")

    if '"tenant_id"' in parameter_list:
        position = parameter_list.index('"tenant_id"')
    else:
        position = -1

    return position


def count_fields_in_sql(sql_query):
    start_fields = sql_query.find("(") + 1
    end_fields = sql_query.find(")")
    fields = sql_query[start_fields:end_fields]
    field_list = fields.split(", ")
    return len(field_list)


def count_value_groups_in_sql(sql_query):
    start_values = sql_query.find("VALUES") + len("VALUES ")
    values_part = sql_query[start_values:]
    group_count = values_part.count("(%s")
    return group_count
