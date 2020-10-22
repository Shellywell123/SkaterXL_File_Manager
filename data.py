

################################################################################
# begining of class
################################################################################

class PyData:
	"""
	class containg dictionaires of flip data
	"""

	def __init__(self,num_of_frames):
		self.num_of_frames = num_of_frames
		self.list_of_zeros = []*num_of_frames

		#ollie/nollie motion

        self.d_theta_h = list(np.linspace(0,180,num_of_frames+1))
        d_theta_r1 = list(np.linspace(0,np.pi,25))
        d_theta_r2 = [0] * (num_of_frames-len(d_theta_r1)+1)
        d_theta_r3 = d_theta_r1+d_theta_r2
        self.d_theta_r = []

        for i in range(1,num_of_frames+1):
            self.theta_r.append(60*np.sin(d_theta_r3))

		self.explain_info = 
				{
				'trick name'   : 'explaination',
				'y_rot_angles' : 'list of angles for rotation around the y axis',
				'z_rot_angles' : 'list of angles for rotation around the z axis',
				'h_rot_angles' : 'list of angles for h*sin(theta)',
				'r_rot_angles' : 'list of angles for ollie motion x rotation'
				}

		self.kickflip_info = 
				{
				'trick name'   : 'kickflip',
				'x_rot_angles' : self.list_of_zeros,
				'y_rot_angles' : list(np.linspace(0,-360,self.num_of_frames+1)),
				'z_rot_angles' : self.list_of_zeros,
				'h_rot_angles' : self.d_theta_h,
				'r_rot_angles' : self.d_theta_r
				}


################################################################################
# End of class
################################################################################
