import numpy as np
import gym
from gym import error, spaces, utils
from gym.utils import seeding

class HVACEnv(Env):
    def __init__(self):
        # Actions we can take, HVACon, HVACoff, stay
        self.action_space = Discrete(3)
        # Temperature array
        self.observation_space = Box(low=np.array([15]), high=np.array([30]),shape=(1,), dtype=np.float32)
        # Set start temp
        self.state = 38 + random.randint(-3,3)
        # Set HVAC length
        self.HVAC_episode = 60
        self.action = 0
        
    def step(self, action):
        
        # Apply action
        # 0 -1 = -1 reduce pump speed reduced temp
        # 1 -1 = 0 
        # 2 -1 = 1 increase pump speed increase temp
        self.state += action -1 
        # Decrement step
        self.HVAC_episode -= 1 
        
        # Calculate reward
        if self.state >=22 and self.state <=26: 
            reward =1 
        else:
            reward = -1
        
        # Check if episode is done 
        if self.HVAC_episode <= 0: 
            done = True
        else:
            done = False
        
        # Apply HVAC temperature noise
        self.state += random.randint(-1,1)
        # Set placeholder for info
        info = {}
        
        
        # Return step information
        return self.state, reward, done, info

    def render(self,mode='human', close=False):

        root = Tk.Tk()
        x =0
        y = 10
        fig = plt.Figure(figsize=(12, 5), dpi=100)
        a = fig.add_subplot(111)
        
                
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.get_tk_widget().grid(column=0,row=1)
        xList = []
        yList = []
        zList = []

        
        l4 = Tk.Label(root, text = "Starting Temp",bg='blue',font=('helvetica', 11, 'bold'))
        l4.grid(row = 1, column = 10, pady = 1)
        l4 = Tk.Label(root, text = self.state)
        l4.grid(row = 1, column = 11, pady = 1)
        
        
        button1=Tk.Button(root, text='Reset', command=env.reset(), bg='blue', font=('helvetica', 11, 'bold'))
        button1.grid(row=2,column=13,pady=3)

        def animate(i,xList,yList):
            xList.append(dt.datetime.now().strftime('%H:%M:%S'))        
            yList.append(self.state)
            xList = xList[-20:]
            yList = yList[-20:]
            a.clear()
            a.plot(xList, yList,label='State(Room Temp)')
            a.set_title("HVAC Room Temp Control")
            a.set_xlabel("Time")
            a.set_ylabel("Room Temperature")
            a.legend()
            plt.xticks(rotation=45, ha='left')
            plt.subplots_adjust(bottom=0.80)

        ani = animation.FuncAnimation(fig, animate, fargs=(xList,yList), interval=500, blit=False)
        Tk.mainloop()
    
    def reset(self):
        
        # Reset HVAC temperature
        self.state = 24 + random.randint(-4,4)
        
        # Reset episode to one minute cal
        self.HVAC_episode = 60
        
        return self.state
    