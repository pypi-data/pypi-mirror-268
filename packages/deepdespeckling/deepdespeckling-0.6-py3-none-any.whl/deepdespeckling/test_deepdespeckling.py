from deepdespeckling.despeckling import despeckle, despeckle_from_coordinates, despeckle_from_crop

image_path = "/Users/hadrienmariaccia/Documents/Projects/deepdespeckling/img/entire/merlin_tests"
destination_directory = "/Users/hadrienmariaccia/Documents/Projects/deepdespeckling/img/entire/merlin_tests"
coordinates_dictionnary = {'x_start': 0,
                           'y_start': 0, 'x_end': 400, 'y_end': 400}

despeckle_from_coordinates(image_path, coordinates_dictionnary, destination_directory,
                           model_name="spotlight")
