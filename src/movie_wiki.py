import json
import os


# TODO: load `wiki_movie_plots.json` from `input` folder
# Be careful : the file size is big so don't display it totally.

def load_movie_list(filepath='input/wiki_movie_plots.json'):
    """Charge et désérialise le fichier JSON contenant les films."""
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)


# TODO: write a function to select only British movies

def classify(movies, origin='British'):
    """Filtre les films selon leur origine."""
    return [movie for movie in movies if movie.get('Origin/Ethnicity') == origin]


# TODO: Save your python object in a new JSON file located in the `output`folder.#  

def save_movie_list(movies, filepath='output/british_movies.json'):
    """Sérialise et sauvegarde les films filtrés dans un nouveau fichier JSON."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(movies, file, indent=2, ensure_ascii=False)


def main():
        all_movies = load_movie_list()
        british_movies = classify(all_movies, origin='British')
        save_movie_list(british_movies)
        print(f"{len(british_movies)} films britanniques sauvegardés dans 'output/british_movies.json'.")

        pass

if __name__ == "__main__":
    main()