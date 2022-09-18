def visualize_dataset(data_dict):
    formatted_dict = {}
    _, labels = data_dict.items()[0]
    dataset = []
    formatted_dict.update{'labels':labels}
    for _,value in data_dict.items()[1:]:
        dataset.append({'data':value})
    formatted_dict.update{'datasets':dataset}
    return formatted_dict
