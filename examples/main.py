from pydictry import Query

P = {"nodes": [
    {"id": 1, "mac": "15:18", "sensor-values": [{"humidity": 15}, {"temperature": 25}]},
    {"id": 2, "mac": "21:28", "sensor-values": [{"humidity": 14}, {"temperature": 26}]},
    {"id": 4, "mac": "21:28", "sensor-values": [{"humidity": 18}, {"movement":  True}]},
    {"id": 3, "mac": "05:08", "sensor-values": [{"humidity": 13}, {"temperature": 27}]}]}


if __name__ == "__main__":

    # collect all node ids
    result_iter = Query(P).select("id").exec()
    node_ids = list(result_iter)

    # collect all temperature readings higher than 25
    result_iter = Query(P).select("temperature").where(lambda t: t > 25).exec()
    temperatures = list(result_iter)

    # use flatten on a collection to perform fine-grained filtering
    # Return nodes with even id number
    result_iter = Query(P).select("nodes").flatten()\
            .where(lambda node: node["id"] % 2 == 0).exec()
    nodes = list(result_iter)

