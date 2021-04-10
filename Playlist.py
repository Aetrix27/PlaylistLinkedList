from Song import Song

class Playlist:
  def __init__(self):
    self.__first_song = None

  # TODO: Create a method called add_song that creates a Song object and adds it to the playlist. This method has one parameter called title.

  def add_song(self, title):
    new_node = Song(title)
    new_node.next = self.__first_song
    self.__first_song = new_node

  # TODO: Create a method called find_song that searches for whether a song exits in the playlist and returns its index.
  # The method has one parameters, title, which is the title of the song to be searched for. If the song is found, return its index. Otherwise, return -1.

  def find_song(self, title):
    current_node = self.__first_song
    counter = 0

    while current_node != None:
      counter += 1
      if title == current_node.get_title():
        return counter-1
      else:
        return -1

  # TODO: Create a method called remove_song that removes a song from the playlist. This method takes one parameter, title, which is the song that should be removed. 

  def remove_song(self, title):
    current_node = self.__first_song
    counter = 0

    while current_node != None:
      counter += 1
      if title == current_node.get_title():
        current_node.get_title()
      else:
        return -1


  # TODO: Create a method called length, which returns the number of songs in the playlist.

  def length(self):
    pass


  # TODO: Create a method called print_songs that prints a numbered list of the songs in the playlist.

  # Example:
  # 1. Song Title 1
  # 2. Song Title 2
  # 3. Song Title 3

  def print_songs(self):
    current_node = self.__first_song

    while current_node != None:
      print(current_node.get_title())
      current_node = current_node.next
