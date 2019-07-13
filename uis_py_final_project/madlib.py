import json
import os
from jinja2 import Template, Environment, meta
from colorama import Fore, Back, Style 


class Madlib:
  def __init__(self, filename):
    self.filename = './madlibs/' +filename + ".json"
    with open( self.filename) as f:
      data = json.load(f)
      # print(data)
      self.template = data["template"]
      self.jinjaTemplate = Template(self.template)
      self.originalStory = data["originalStory"]
      self.prompts = data["prompts"]
      self.stories = data["stories"]

  def printOriginalStory(self):
    print(Fore.GREEN + self.jinjaTemplate.render(self.originalStory))
    print(Style.RESET_ALL) 

  def play(self):
    userStory = {}
    #Loop through each key stored in the prompts dictionary
    #and add that key as the key in the dictionary userStory
    #and add the value stored at that key into the dictionary userStory
    for key in self.prompts:
      response = input("Enter " + self.prompts[key] + ": ")
      userStory[key] = response
    #print(self.jinjaTemplate.render(userStory))
    return userStory

  def printStory(self, story):
    print(Fore.YELLOW + self.jinjaTemplate.render(story))
    print(Style.RESET_ALL) 

  def saveStory(self, story, storyName):
    self.stories[storyName] = story
    self._saveToFile()

  def _saveToFile(self):
    with open(self.filename, 'w') as f:
      data = {
        "template": self.template,
        "originalStory": self.originalStory,
        "prompts": self.prompts,
        "stories": self.stories
      }
      json.dump(data, f, indent=4)

  def printNumStories(self):
    print(len(self.stories.keys()))

  def printStoryNames(self):
    storyNames = self.stories.keys()
    for key in storyNames:
      print(key)

  def printUserStory(self, storyName):  
    print(Fore.YELLOw + self.jinjaTemplate.render(self.stories[storyName])) 
    print(Style.RESET_ALL)      
    

  @classmethod
  def createMadlib(cls):
    template = input("Type your story with double curly braces around each variable name (e.g. {{Name}} is going to {{country}}.)")
    env = Environment()
    ast = env.parse(template)
    variables = list(meta.find_undeclared_variables(ast))
    print(variables)
    print()

    originalStory = {}
    for var in variables:
      value = input("What is the value of {{" + var + "}} in your original story?")
      originalStory[var] = value
    print(originalStory)
    print()

    prompts = {}
    for var in variables:
      prompt = input("What is the description of {{" + var + "}}?")
      prompts[var] = prompt
    print(prompts)
    print()

    madlib = {"template": template,
              "originalStory": originalStory,
              "prompts": prompts,
              "stories": {}
    }

    madlibName = input("What do you want to name this madlib?")
    filename = './madlibs/' + madlibName + ".json"

    with open(filename, 'w') as f:
      json.dump(madlib, f, indent=4)

    print("madlib saved successfully")



  @classmethod
  def printMadlibTitles(cls):
    #print("called")
    filenames = os.listdir('./madlibs')
    filenames = [f[:-5] for f in filenames if ".json" in f]
    print("Madlib files available to choose from: ")
    for f in filenames:
      print(" - " + f)






  
