from bing_image_downloader import downloader
query_string = input("enter your search keyword:")
x = int(input("number of images you want:"))
downloader.download(query_string, limit= x,  output_dir='dataset', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)
