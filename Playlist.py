from Song import Song

class Playlist:
  def __init__(self):
    self.__first_song = None

  def add_song(self, title):
    new_song = Song()
    new_song.set_title(title)
    new_song.set_next_song(self.__first_song)
    self.__first_song = new_song

  def find_song(self, title):
    current_node = self.__first_song
    titleFound = False
    index = 0

    while current_node != None:
      if title == current_node.get_title():
        return index
        titleFound = True
   
      current_node = current_node.get_next_song()
      index += 1

    if titleFound == False:
      return -1
     

  def remove_song(self, title):
    prev_node = None
    current_node = self.__first_song
    while current_node != None:
      if current_node.get_title() == title:
        if prev_node != None:
          prev_node.set_next_song(current_node.get_next_song())
          break
        else:
          current_node.set_next_song(self.__first_song)
          break
      prev_node = current_node
      current_node = current_node.get_next_song()
        

  def length(self):
    counter = 0
    current_node = self.__first_song

    while current_node != None:
      counter += 1
      current_node = current_node.get_next_song()

    return counter

  def print_songs(self):
    counter= 1
    current_node = self.__first_song
    while current_node != None:
      print(f'# {counter}. {current_node}')
      current_node = current_node.get_next_song()
      counter += 1
