from highrise import BaseBot
from highrise import __main__
from collections import UserDict
from asyncio import run as arun
from highrise.models import SessionMetadata, User
from highrise.models import Position
from highrise.models import SessionMetadata, User, CurrencyItem, Item, AnchorPosition, Reaction, ModerateRoomRequest, Position
from highrise import BaseBot, User, Position, SessionMetadata
import random
import asyncio
from highrise import BaseBot, __main__
from highrise.models import (AnchorPosition, Item, Position, User,)
from highrise import *
from highrise.models import *
import time
from asyncio import Task
from highrise.__main__ import *
from highrise.models import (AnchorPosition, CurrencyItem,Item,Position,SessionMetadata,User,)

emote_list : list[tuple[str, str]] = [('1', 'idle-sleep'), ('83', 'idle_singing'), ('82', 'emote-greedy'), ('81', 'emote-snowball'), ('79', 'emote-teleporting'), ('80', 'emote-swordfight'), ('78', 'dance-Pennywise'), ('77', 'emote-telekinesis'), ('76', 'emote-pose8'), ('75', 'emote-pose7'), ('74', 'emote-pose3'), ('73', 'emote-Pose5'), ('72', 'emoji-flex'), ('71', 'emoji-gagging'), ('70', 'emote-maniac'), ('69', 'emote-snake'), ('68', 'emote-frog'), ('67', 'emote-superpose'), ('66', 'emote-cute'), ('65', 'dance-weird'), ('64', 'dance-icescream'), ('63', 'emote-gravity'), ('62', 'emote-fashionista'), ('61', 'idle-uwu'), ('60', 'idle-dance-tiktok4'), ('59', 'dance-tiktok10'), ('58', 'dance-anime'), ('57', 'emote-shy2'), ('3', 'idle-sad'), ('4', 'idle-loop-tired'), ('5', 'idle-loop-sitfloor'), ('Shy', 'idle-loop-shy'), ('7', 'idle-enthusiastic'), ('8', 'idle-dance-headbobbing'), ('9', 'emote-yes'), ('10', 'emote-wave'), ('11', 'emote-tired'), ('12', 'emote-think'), ('13', 'emote-theatrical'), ('14', 'emote-snowangel'), ('6', 'emote-shy'), ('15', 'emote-sad'), ('16', 'emote-peace'), ('17', 'emote-no'), ('18', 'emote-model'), ('19', 'emote-lust'), ('20', 'emote-laughing2'), ('21', 'emote-laughing'), ('22', 'emote-kiss'), ('Super Kick', 'emote-kicking'), ('23', 'emote-jumpb'), ('24', 'emote-judochop'), ('25', 'emote-hot'), ('26', 'emote-hello'), ('27', 'emote-happy'), ('28', 'emote-exasperatedb'), ('29', 'emote-exasperated'), ('30', 'emote-death2'), ('Revival', 'emote-death'), ('31', 'emote-dab'), ('32', 'emote-curtsy'), ('33', 'emote-confused'), ('34', 'emote-cold'), ('35', 'emote-charging'), ('36', 'emote-bunnyhop'), ('37', 'emote-bow'), ('38', 'emote-boo'), ('Home Run!', 'emote-baseball'), ('39', 'emote-apart'), ('40', 'emoji-thumbsup'), ('41', 'emoji-there'), ('42', 'emoji-sneeze'), ('43', 'emoji-smirking'), ('44', 'emoji-sick'), ('Gasp', 'emoji-scared'), ('Punch', 'emoji-punch'), ('45', 'emoji-dizzy'), ('46', 'emoji-cursing'), ('Sob', 'emoji-crying'), ('47', 'emoji-clapping'), ('48', 'emoji-celebrate'), ('Arrogance', 'emoji-arrogance'), ('49', 'emoji-angry'), ('Vogue Hands', 'dance-voguehands'), ('50', 'dance-tiktok8'), ("51", 'dance-tiktok2'), ('52', 'dance-spiritual'), ("53", 'dance-shoppingcart'), ('54', 'dance-russian'), ('55', 'dance-macarena'), ('56','dance-blackpink'),]



    
emote_durations = { 
    "2": 15,
    "3": 10,
    "4": 10,
    "5": 15,
    "6": 15,
    "7": 15,
    "8": 15,
    "9": 4,
    "10": 3,
    "11": 5,
    "12": 5,
    "13": 10,
    "14": 7,
    "15": 5,
    "16": 6,
    "17": 4,
    "18": 7,
    "19": 5,
    "20": 10,
    "21": 4,
    "22": 4,
    "23": 10,
    "24": 6,
    "25": 6,
    "26": 4,
    "27": 4,
    "28": 10,
    "29": 10,
    "***": 10,
    "31": 10,
    "32": 3,
    "33": 10,
    "34": 10,
    "35": 9,
    "36": 10,
    "37": 4,
    "38": 10,
    "39": 10,
    "40": 4,
    "41": 10,
    "42": 10,
    "43": 10,
    "44": 10,
    "45": 10,
    "46": 10,
    "47": 10,
    "48": 10,
    "49": 10,
    "50": 10,
    "51": 10,
    "52": 10,
    "53": 10,
    "54": 10,
    "55": 10,
    "56": 10,
    "57": 9, 
    "58": 10,
    "59": 10,
    "60": 8,
    "61": 10,
    "62": 10, 
    "63": 10,
    "64": 10,
    "65": 10,
    "66": 10,
    "67": 10,
    "68": 10,
    "69": 10,
    "70": 6,
    "71": 10,
    "72": 10,
    "73": 10,
    "74": 10,
    "75": 10,
    "76": 10,
    "77": 10,
    "78": 10,
    "79": 10,
    "80": 10,
    "81": 10,
    "82": 10,
    "83": 10,    

}

class BotDefinition:
  def __init__(self, bot, room_id, api_token):
      self.bot = bot
      self.room_id = room_id
      self.api_token = api_token

class MyBot(BaseBot):
  
    
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.following_user = None
    self.banned_users = {}
    self.following_username = None
    super().__init__()
    self.user_positions = {} 

  async def on_user_move(self, user: User, pos: Position) -> None:
     self.user_positions[user.username] = pos
     print (f"{user.username} moved to {pos}")


  async def on_start(self, Session_Metadata: SessionMetadata):
    await self.send_continuous_random_emote_in_dance_floor()

  async def send_continuous_random_emote_in_dance_floor(self):
    emote_duration_mapping = {
      'emote-float': 8.995302,
      'emote-frog': 14.55257,
      'emote-hot': 4.353037,
      'emote-maniac': 4.906886,
      'emote-gravity': 8.955966,
      'dance-russian': 10.252905,
      'emote-zombierun': 12.922772,
      'emore-punkguitar': 9.365807,
      'idle-guitar': 13.229398,
      'emote-teleporting': 11.7676,
      'dance-tiktok10': 8.225648,
      'dance-tiktok2': 10.392353,
      'idle-dance-tiktok4': 15.500708,
      'dance-tiktok8': 10.938702,
      'dance-tiktok9': 11.892918,
      'dance-shoppingcart': 4.316035,
      'dance-blackpink': 7.150958,
      'dance-anime': 8.46671,
      'emote-telekinesis': 10.492032,
      'emote-energyball':7.575354,
      'dance-icecream': 14.769573,
      'emote-snowangel': 6.218627,
      'idle-singing': 10.260182,
      'emote-snake': 5.262578,
      'dance-weird': 21.556237,
      'dance-wrong': 12.422389,
      'emote-headblowup': 11.667537,
      'emote-boxer': 5.555702,
      'dance-employee': 8,
      'emote-celebrationstep': 3.353703,
      'emote-iceskating': 7.299156,
      'dance-kawai': 10.290789,
      'dance-pinguin': 11.58291,
      'emote-timejump': 4.007305,
      'emote-swordfight': 5.914365,
      'emote-astronaut': 13.791175,
      'dance-jinglebell': 10.958832,
      'emote-hyped': 7.492423,
      'emote-looping': 9.0,
      'dance-creepypuppet': 6.416121,
      'emote-sleigh': 11.333165,
      'emote-launch': 9.4,
      'dance-tiktok11': 10.8,

    }
    position_bounds = {
            'x': (14.5, 16.5),
            'y': (0.3000030517578125, 0.3000030517578125),  # Constant Y
            'z': (25.5, 28.5),
    }

    last_emote_times = {}
    last_emote_durations = {}

    while True:
        try:
            room_users = await self.highrise.get_room_users()
            current_time = time.time()

            # Find if any user is currently emoting
            emoting_users = {
                user_id: last_emote_times[user_id]
                for user_id in last_emote_times
                if current_time - last_emote_times[user_id] < last_emote_durations[user_id]
            }

            # Select a new emote if no one is emoting
            if not emoting_users:
                emote_name = random.choice(list(emote_duration_mapping.keys()))

            for user, position in room_users.content:
                if isinstance(position, (Position, AnchorPosition)):
                    if isinstance(position, Position):
                        x, y, z = position.x, position.y, position.z
                    else:
                        continue  # Skip processing for AnchorPosition for now
                    # Check if the user's position is within the defined box-shaped region
                    if (
                        position_bounds['x'][0] <= x <= position_bounds['x'][1] and
                        position_bounds['y'][0] <= y <= position_bounds['y'][1] and
                        position_bounds['z'][0] <= z <= position_bounds['z'][1]
                    ):
                        last_emote_time = last_emote_times.get(user.id, 0)
                        time_difference = current_time - last_emote_time

                        # Only emote if no one else is currently emoting in the area
                        if not emoting_users:
                            emote_duration = emote_duration_mapping[emote_name]
                            
                            if time_difference >= last_emote_durations.get(user.id, 0):
                                await self.highrise.send_emote(emote_name, user.id)
                                last_emote_times[user.id] = current_time
                                last_emote_durations[user.id] = emote_duration

        except Exception as e:
            print(f"An error occurred: {e}")

        await asyncio.sleep(1) 



  
      
  async def on_whisper(self, user: User, message: str):
    if user.username == "T9s": 
      await self.highrise.chat(message)

  async def loop(self: BaseBot, user: User, message: str) -> None:
      async def loop_emote(self: BaseBot, user: User, emote_name: str) -> None:
          emote_id = ""
          for emote in emote_list:
              if emote[0].lower() == emote_name.lower():
                  emote_id = emote[1]
                  break
          if emote_id == "":
              await self.highrise.chat("Invalid emote")
              return

          await self.highrise.chat(f"@{user.username} is looping {emote_name}")

          # الحصول على مدة الرقصة
          emote_duration = emote_durations.get(emote_name)
          if emote_duration is None:
              await self.highrise.send_whisper(user.id,f"The emote {emote_name} does not have a specified duration.")
              return

          while True:
              try:
                  await self.highrise.send_emote(emote_id, user.id)
              except:
                  await self.highrise.send_whisper(user.id,f"Sorry, @{user.username}, this emote isn't free or you don't own it.")
                  return

              # فترة انتظار لمدة الرقصة
              await asyncio.sleep(emote_duration)

              room_users = (await self.highrise.get_room_users()).content
              user_in_room = False
              for room_user, position in room_users:
                  if room_user.id == user.id:
                      user_in_room = True
                      break
              if not user_in_room:
                  break

      try:
          splited_message = message.split(" ")
          # The emote name is every string after the first one
          emote_name = " ".join(splited_message[1:])
      except:
          await self.highrise.chat("Invalid command format. Please use '/loop <emote name>.")
          return
      else:   
          taskgroup = self.highrise.tg
          task_list: list[Task] = list(taskgroup._tasks)
          for task in task_list:
              if task.get_name() == user.username:
                  # Removes the task from the task group
                  task.cancel()

          room_users = (await self.highrise.get_room_users()).content
          user_list = [room_user.username for room_user, pos in room_users]

          taskgroup.create_task(coro=loop_emote(self, user, emote_name))
          task_list: list[Task] = list(taskgroup._tasks)
          for task in task_list:
              if task.get_coro().__name__ == "loop_emote" and task.get_name() not in user_list:
                  task.set_name(user.username)

  async def stop_loop(self: BaseBot, user: User, message: str) -> None:
      taskgroup = self.highrise.tg
      task_list: list[Task] = list(taskgroup._tasks)
      for task in task_list:
          print(task.get_name())
          if task.get_name() == user.username:
              task.cancel()
              await self.highrise.send_whisper(user.id,f"Stopping your emote loop, {user.username}!")
              return
      await self.highrise.send_whisper(user.id, f"You're not looping any emotes, {user.username}")
      return

  async def on_user_join(self, user: User, position: Position | AnchorPosition):
        room_users = await self.highrise.get_room_users()
        if any(room_user.id == user.id for room_user, _ in room_users.content):
            try:
                await self.highrise.send_whisper(user.id,
                    f"Welcome {user.username} to BAR DATE❣️"
                )
                await self.highrise.send_whisper(
                    user.id,
                    f" Loop 1-83 for free emotes \n Stop that it stops "
                )
            except Exception as e:
                print(f"Failed to send whisper: {e}")

  async def run(self, room_id, token):
    definitions = [BotDefinition(self, room_id, token)]
    await __main__.main(definitions)

  async def teleport_user_next_to(self, target_username: str,
                                  requester_user: User):

    room_users = await self.highrise.get_room_users()
    requester_position = None

    for user, position in room_users.content:
      if user.id == requester_user.id:
        requester_position = position
        break
    for user, position in room_users.content:
      if user.username.lower() == target_username.lower():
        z = requester_position.z
        new_z = z + 1

        user_dict = {
            "id":
            user.id,
            "position":
            Position(requester_position.x, requester_position.y, new_z, requester_position.facing)
        }
        await self.highrise.teleport(user_dict["id"], user_dict["position"])

  
  
  async def on_chat(self, user: User, message: str):
    
    if message.startswith("come") and user.username in ["T9s", "yasu2"]:
      response = await self.highrise.get_room_users()
      your_pos = None
      for content in response.content:
        if content[0].id == user.id:
          if isinstance(content[1], Position):
            your_pos = content[1]
            break
      if not your_pos:
        await self.highrise.send_whisper(user.id, f"Invalid coordinates")
        return
      await self.highrise.chat("I,m coming ")
      await self.highrise.walk_to(your_pos)

    if message.startswith("Float"):
      await self.highrise.send_emote("emote-float", user.id)
    if message.startswith("Tiktok2"):
      await self.highrise.send_emote("dance-tiktok2", user.id)
    if message.startswith("pose1"):
      await self.highrise.send_emote("emote-pose1", user.id)
    if message.startswith("Russian"):
      await self.highrise.send_emote("dance-russian", user.id)
    if message.startswith("Sing"):
      await self.highrise.send_emote("idle_singing", user.id)
    if message.startswith("Enth"):
      await self.highrise.send_emote("idle-enthusiastic", user.id)
    if message.startswith("Casual"):
      await self.highrise.send_emote("idle-dance-casual", user.id)
    if message.startswith("sit"):
      await self.highrise.send_emote("idle-loop-sitfloor", user.id)
    if message.startswith("Lust"):
      await self.highrise.send_emote("emote-lust", user.id)
    if message.startswith("Creedy"):
      await self.highrise.send_emote("emote-greedy", user.id)
    if message.startswith("Bow"):
      await self.highrise.send_emote("emote-bow", user.id)
    if message.startswith("Curtsy"):
      await self.highrise.send_emote("emote-curtsy", user.id)
    if message.startswith("Snow"):
      await self.highrise.send_emote("emote-snowball", user.id)
    if message.startswith("Angel"):
      await self.highrise.send_emote("emote-snowangel", user.id)
    if message.startswith("Confused"):
      await self.highrise.send_emote("emote-confused", user.id)
    if message.startswith("Teleport"):
      await self.highrise.send_emote("emote-teleporting", user.id)
    if message.startswith("Swordfight"):
      await self.highrise.send_emote("emote-swordfight", user.id)
    if message.startswith("Energy"):
      await self.highrise.send_emote("emote-energyball", user.id)
    if message.startswith("Tiktok8"):
      await self.highrise.send_emote("dance-tiktok8", user.id)
    if message.startswith("Blackpink"):
      await self.highrise.send_emote("dance-blackpink", user.id)
    if message.startswith("Model"):
      await self.highrise.send_emote("emote-model", user.id)
    if message.startswith("Penny"):
      await self.highrise.send_emote("dance-pennywise", user.id)
    if message.startswith("Tiktok10"):
      await self.highrise.send_emote("dance-tiktok10", user.id)
    if message.startswith("Telekinesis"):
      await self.highrise.send_emote("emote-telekinesis", user.id)
    if message.startswith("Hot"):
      await self.highrise.send_emote("emote-hot", user.id)
    if message.startswith("Weird"):
      await self.highrise.send_emote("dance-weird", user.id)
    if message.startswith("Pose7"):
      await self.highrise.send_emote("emote-pose7", user.id)
    if message.startswith("Pose8"):
      await self.highrise.send_emote("emote-pose8", user.id)
    if message.startswith("Pose3"):
      await self.highrise.send_emote("emote-pose3", user.id)
    if message.startswith("Pose5"):
      await self.highrise.send_emote("emote-pose5", user.id)
    if message.startswith("kiss"):
      await self.highrise.send_emote("emote-kiss", user.id)

    if message.startswith("Laughing"):
      await self.highrise.send_emote("emote-laughing", user.id)
    if message.startswith("cursing"):
      await self.highrise.send_emote("emoji-cursing", user.id)
    if message.startswith("flex"):
      await self.highrise.send_emote("emoji-flex", user.id)
    if message.startswith("gagging"):
      await self.highrise.send_emote("emoji-gagging", user.id)
    if message.startswith("celebrate"):
      await self.highrise.send_emote("emoji-celebrate", user.id)
    if message.startswith("macarena"):
      await self.highrise.send_emote("dance-macarena", user.id)
    if message.startswith("charging"):
      await self.highrise.send_emote("emote-charging", user.id)
    if message.startswith("shopp"):
      await self.highrise.send_emote("dance-shoppingcart", user.id)
    if message.startswith("maniac"):
      await self.highrise.send_emote("emote-maniac", user.id)
    if message.startswith("snake"):
      await self.highrise.send_emote("emote-snake", user.id)
    if message.startswith("frog"):
      await self.highrise.send_emote("emote-frog", user.id)
    if message.startswith("superpose"):
      await self.highrise.send_emote("emote-superpose", user.id)
    if message.startswith("cute"):
      await self.highrise.send_emote("emote-cute", user.id)
    if message.startswith("tiktok9"):
      await self.highrise.send_emote("dance-tiktok9", user.id)
    if message.startswith("weird"):
      await self.highrise.send_emote("dance-weird", user.id)
    if message.startswith("cutey"):
      await self.highrise.send_emote("emote-cutey", user.id)
    if message.startswith("punkguitar"):
      await self.highrise.send_emote("emote-punkguitar", user.id)
    if message.startswith("zombierun"):
      await self.highrise.send_emote("emote-zombierun", user.id)
    if message.startswith("fashi"):
      await self.highrise.send_emote("emote-fashionista", user.id)
    if message.startswith("gravity"):
      await self.highrise.send_emote("emote-gravity", user.id)
    if message.startswith("icecream"):
      await self.highrise.send_emote("dance-icecream", user.id)
    if message.startswith("wrong"):
      await self.highrise.send_emote("dance-wrong", user.id)
    if message.startswith("uwu"):
      await self.highrise.send_emote("idle-uwu", user.id)
    if message.startswith("tiktok4"):
      await self.highrise.send_emote("idle-dance-tiktok4", user.id)
    if message.startswith("shy2"):
      await self.highrise.send_emote("emote-shy2", user.id)
    if message.startswith("anime"):
      await self.highrise.send_emote("dance-anime", user.id)


    
    emotes = [
      "emote-float",
      "dance-tiktok2",
      "emote-pose1",
      "dance-russian",
      "idle_singing",
      "idle-enthusiastic",
      "idle-dance-casual",
      "idle-loop-sitfloor",
      "emote-lust",
      "emote-greedy",
      "emote-bow",
      "emote-curtsy",
      "emote-snowball",
      "emote-snowangel",
      "emote-confused",
      "emote-teleporting",
      "emote-swordfight",
      "emote-energyball",
      "dance-tiktok8",
      "dance-blackpink",
      "emote-model",
      "dance-pennywise",
      "dance-tiktok10",
      "emote-telekinesis",
      "emote-hot",
      "dance-weird",
      "emote-pose7",
      "emote-pose8",
      "emote-pose3",
      "emote-pose5",
      "emote-kiss",
      "emote-laughing",
      "emoji-cursing",
      "emoji-flex",
      "emoji-gagging",
      "emoji-celebrate",
      "dance-macarena",
      "emote-charging",
      "dance-shoppingcart",
      "emote-maniac",
      "emote-snake",
      "emote-frog",
      "emote-superpose",
      "emote-cute",
      "dance-tiktok9",
      "dance-weird",
      "emote-cutey",
      "emote-punkguitar",
      "emote-zombierun",
      "emote-fashionista",
      "emote-gravity",
      "dance-icecream",
      "dance-wrong",
      "idle-uwu",
      "idle-dance-tiktok4",
      "emote-shy2",
      "dance-anime"
    ]

    if message.startswith("emotes"):
          # اختر إيموجي عشوائي من القائمة
          random_emote = random.choice(emotes)
          # أرسل الإيموجي المختار
          await self.highrise.send_emote(random_emote, user.id)

    
    allowed_users = [
        "T9s", "HisTigerPrincess", "jc.kim0","iiLitTea","iiDeima","X_Itachi_381","vivi.rbw","_GrumpyKitty_0.1","Jungfrau",'Okean0s','NoxxPlay','Hrvyn','Maavii.8','Ayumii28','yasu2'
    ]
    if message.startswith("summon") and user.username in [
       "T9s", "HisTigerPrincess", "jc.kim0","iiLitTea","iiDeima","X_Itachi_381","vivi.rbw","_GrumpyKitty_0.1","Jungfrau",'Okean0s','NoxxPlay','Hrvyn','Maavii.8','Ayumii28','yasu2'
    ]:
      allowed_users = message.split("@")[-1].strip()
      if allowed_users in allowed_users:
        await self.teleport_user_next_to(allowed_users, user)


    if message.startswith("to") and user.username in [
       "T9s", "HisTigerPrincess", "jc.kim0","iiLitTea","iiDeima","X_Itachi_381","vivi.rbw","_GrumpyKitty_0.1","Jungfrau",'Okean0s','NoxxPlay','Hrvyn','Maavii.8','Ayumii28','yasu2'
    ]:
      words = message.split(" ")
      if len(words) > 1:
          target_username = words[1].replace("@", "")
          if target_username in self.user_positions:
              target_position = self.user_positions[target_username]
              await self.highrise.teleport(user.id, target_position)
              await self.highrise.chat(f"You have been pulled to a site {target_username}")
          else:
              await self.highrise.chat("User location not specified.")
      else:
          await self.highrise.chat("Username must be specified.")
    
    if message.lower().startswith("loop "):
      await self.loop(user, message)
    elif message.lower().startswith("stop"):
      await self.stop_loop(user, message)


    if message.lower().startswith("!help"):
      await self.highrise.send_whisper(
          user.id,
          " celebrate , macarena , charging , shopp , maniac , snake  , frog , superpose , cute , tiktok9 , weird , cutey ,  punkguitar , zombierun , fashi , gravity , icecream , wrong , uwu , tiktok4 , shy2 , anime"
      )

    if message.lower().startswith("!help"):
      await self.highrise.send_whisper(
          user.id,
          "Model , Penny , Tiktok10 , Telekinesis , Hot , Weird , Pose7 , Pose8 , Pose3 , Pose5 , kis , Laughing , cursing , flex , gagging , Blackpink , Tiktok8"
      )

    if message.lower().startswith("!help"):
      dance_list = [
          "Float",
          "Tiktok2",
          "pose1",
          "Russian",
          "Sing",
          "Enth",
          "Casual",
          "sit",
          "Lust",
          "Creedy",
          "Bow",
          "Curtsy",
          "Snow",
          "Angel",
          "Confused",
          "Teleport",
          "Swordfight",
          "Energy",
      ]

      # Convert the list to a comma-separated string
      dance_list_str = ", ".join(dance_list)

      # Send the message
      await self.highrise.send_whisper(user.id, dance_list_str)
  


     

      
    if message.startswith("!kick") and user.username in [
         "T9s", "HisTigerPrincess", "jc.kim0","iiLitTea","iiDeima","X_Itachi_381","vivi.rbw","_GrumpyKitty_0.1","Jungfrau",'Okean0s','NoxxPlay','Hrvyn','Maavii.8','Ayumii28','yasu2'
      ]:
          
            
          # فصل الرسالة إلى أجزاء
          parts = message.split()

          # التحقق من صحة تنسيق الأمر "kick @username"
          if len(parts) != 2:
              await self.highrise.chat("Invalid kick command format.")
              return

          # التحقق مما إذا كان هناك @ في الرسالة
          if "@" not in parts[1]:
              username = parts[1]
          else:
              username = parts[1][1:]

          # التحقق مما إذا كان المستخدم في الغرفة
          room_users = (await self.highrise.get_room_users()).content
          user_id = None
          for room_user, pos in room_users:
              if room_user.username.lower() == username.lower():
                  user_id = room_user.id
                  break

          if user_id is None:
              await self.highrise.chat("User not found, please specify a valid user and coordinate")
              return

          # طرد المستخدم
          try:
              await self.highrise.moderate_room(user_id, "kick")
          except Exception as e:
              await self.highrise.chat(f"{e}")
              return

          # إرسال رسالة إلى الدردشة
          await self.highrise.chat(f"{username} has been kicked from the room.")
      
    if message == "!1st":
      await self.highrise.teleport(user.id, Position(6.5, 0.0, 3.5))

    if message == "!2nd":
      await self.highrise.teleport(user.id, Position(11.5, 8.25, 5.5))

    

    if message.startswith("vip") and user.username in [
       "T9s", "HisTigerPrincess", "jc.kim0","iiLitTea","iiDeima","X_Itachi_381","vivi.rbw","_GrumpyKitty_0.1","Jungfrau",'Okean0s','NoxxPlay','Hrvyn','Maavii.8','Ayumii28','yasu2'
    ]:
      await self.highrise.teleport(user.id, Position(11.5, 15.0, 5.5))

    
    if message.startswith("mods") and user.username in [
       "T9s", "HisTigerPrincess", "jc.kim0","iiLitTea","iiDeima","X_Itachi_381","vivi.rbw","_GrumpyKitty_0.1","Jungfrau",'Okean0s','NoxxPlay','Hrvyn','Maavii.8','Ayumii28','yasu2'
    ]:
      await self.highrise.teleport(user.id, Position(13.5, 19.0, 3  ))
   
   
