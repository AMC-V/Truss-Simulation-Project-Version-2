import vpython as vp
import numpy as np
#=================================================================
# region method overloads for convenions
def arrow(**kid):
    return vp.arrow(pos = kid["pos"], axis = kid["axis"], round = True)

def vec(x,y,z):
    return vp.vec(x,y,z)

def sphere(**kid):
    return vp.sphere(pos = kid["pos"], radius = 0.1, make_trail = False, color = 1/255 * vec(255,150,0))

def radians(number):
    return vp.radians(number)

def sin(number):
    return vp.sin(number)

def cos(number):
    return vp.cos(number)

def arange(min, max, change):
    return vp.arange(min, max, change)

def cylinder(**kid):
    return vp.cylinder(pos = kid["pos"], axis = kid["axis"], radius = 0.1) #, color = kid["color"])

def pi():
    return vp.pi

def ring(**kid):
    return vp.ring(pos = kid["pos"], axis = kid["axis"], radius = kid["radius"])

def rate(number):
    return vp.rate(number)

def cross(number_1, number_2):
    return vp.cross(number_1, number_2)

def mag(number):
    return vp.mag(number)

def hat(number):
    return vp.hat(number)

def sqrt(number):
    return vp.sqrt(number)
# endregion
#=================================================================

class GraphicsTools():
    number_of_nodes = 0
    number_of_current_members = 0
    number_of_equations = 0

    list_of_nodes = [] # Will contain all nodes and serves as the backup list to check incoming data
    list_of_spheres = []
    list_of_labels = []
    
    list_of_force = []
    list_of_angle = []
    list_of_force_arrows = []
    list_of_force_final = []
    
    list_of_elements = [] # Will contain all the elements, connections between nodes, also the number of unknowns
    list_of_elements_label = []
    element_visual_list = [] # will hold something
    list_of_unknowns = [] # based on the amount of elements
    
    number_of_backend_rollers = 0
    list_of_visual_rollers = []
    list_of_rollers = []
    list_of_rollers_ground = []
    
    number_of_backend_pins = 0
    list_of_visual_pins = []
    list_of_pins = []
    list_of_pins_spacing = []
    list_of_pins_ground = []
    
    known_forces = []
    unknown_forces = []
    master_matrix = []
    roller_matrix = 0
    pin_matrix = 0
    engineering_support_matrix = 0
    coeffeicent_matrix = []

    def __init__(self): # The constructor for this class that will always be called when first created
        # region Gobal Coordiante System 
        origin = vec(0, 0, 0)
        axis = vp.sphere(pos = origin, radius = 10)  # Here radius is length of axis
        axis.l = axis.radius  # Lenght of axis arrows
        axis.s = axis.radius/100         # Radius of axis arrows, so if lenght is 5 then radius is 0.05
        axis.f = 'monospace'
        axis.toffset = 0.05
        axis.visible = False
        op = 0.25

        pos_x_axis = arrow(pos = origin, axis = vec(axis.l, 0, 0))
        pos_x_axis.shaftwidth = axis.s
        pos_x_axis.color = vec(1, 0, 0)
        pos_x_axis.opacity = op

        pos_x_axis_label = vp.label(pos = pos_x_axis.pos + pos_x_axis.axis + vec(axis.toffset, 0, 0), 
                text='+x', height = 16, border = 4, font = axis.f, line = False, opacity = 0, box = False)
                
        neg_x_axis = arrow(pos = origin, axis = vec(-axis.l, 0, 0))
        neg_x_axis.shaftwidth = axis.s
        neg_x_axis.color = vec(1, 0, 0)
        neg_x_axis.opacity = op

        neg_x_axis_label = vp.label(pos = neg_x_axis.pos + neg_x_axis.axis + vec(-axis.toffset, 0, 0), 
                text='-x', height = 16, border = 4, font = axis.f, line = False, opacity = 0, box = False)
                
        pos_y_axis = arrow(pos = origin, axis = vec(0, axis.l, 0))
        pos_y_axis.shaftwidth = axis.s 
        pos_y_axis.color = vec(0, 1, 0)
        pos_y_axis.opacity = op

        pos_y_axis_label = vp.label(pos = pos_y_axis.pos + pos_y_axis.axis + vec(0, axis.toffset, 0), 
                text='+y', height = 16, border = 4, font = axis.f, line = False, opacity = 0, box = False)
                
        neg_y_axis = arrow(pos = origin, axis = vec(0, -axis.l, 0))
        neg_y_axis.shaftwidth = axis.s
        neg_y_axis.color = vec(0, 1, 0)
        neg_y_axis.opacity = op

        neg_y_axis_label = vp.label(pos = neg_y_axis.pos + neg_y_axis.axis + vec(0, -axis.toffset, 0), 
                text='-y', height = 16, border = 4,font = axis.f, line = False, opacity = 0, box = False)

        # pos_z_axis = arrow(pos = origin, axis = vec(0,0,axis.l))
        # pos_z_axis.shaftwidth = axis.s
        # pos_z_axis.color = vec(0, 0, 1)
        # pos_z_axis.opacity = op

        # pos_z_axis_label = vp.label(pos = pos_z_axis.pos + pos_z_axis.axis + vec(0, axis.toffset, 0), 
        #         text='+z', height = 16, border = 4, font = axis.f, line = False, opacity = 0, box = False)
                
        # neg_z_axis = arrow(pos = origin, axis = vec(0,0,-axis.l))
        # neg_z_axis.shaftwidth = axis.s
        # neg_z_axis.color = vp.vec(0, 0, 1)
        # neg_z_axis.opacity = op

        #neg_z_axis_label = vp.label(pos = neg_z_axis.pos + neg_z_axis.axis + vec(0, -axis.toffset, 0), 
        #        text='-z', height = 16, border = 4,font = axis.f, line = False, opacity = 0, box = False)
        #=================================================================
        # endregion
        
    def node_creation(self, x, y, current_node): # intended to handle new nodes and existing nodes no forces, both cases work
        print(f"Number of nodes in backend list is {self.number_of_nodes} and current node number is {current_node} from gui.")
        
        # so node number doesn't exist in list of nodes
        if current_node > self.number_of_nodes and current_node - 1 == self.number_of_nodes: 
            print(f"Creating node {current_node}-")
            # create sphere and label to visually represent node and added to list so can be used to modify a node's properties
            self.list_of_spheres.append(sphere(pos = vec(x, y, 0))) 
            self.list_of_labels.append(vp.label(pos = vec(x, y, 0), text = f"{current_node}", xoffset = 5, yoffset = 10, space = 1, 
                    height = 16, border = 4, font = 'monospace', box = False, opacity = 0, color = 1/255 * vec(255,150,0)))
            self.list_of_nodes.append(vec(x, y, 0)) # basically only holds a node's position, 3D will used z position
            
            # Very important that the assicoted force to a node is created here, as the force creation method relies on the results here
            self.list_of_force.append(0) # leave a placeholder in the list for the node's force
            self.list_of_angle.append(0) # leave a placeholder in the list for the node's angle
            self.list_of_force_final.append(vec(0,0,0))
            print(f"act heree {len(self.list_of_force_final)}")
            self.list_of_force_arrows.append(vp.arrow(pos = vec(0,0,0,), axis = vec(0,0,0), color = 1/255 * vec(236, 215, 16), opacity = 0))
    
            self.number_of_nodes += 1
            print(f"Node {current_node} created successfully-")
        
        # then we are skipping a few nodes in the line and need to actualize the skipped, can opimized
        elif current_node > self.number_of_nodes and current_node - 1 != self.number_of_nodes:
            print("Trying to actualize a node without actualizing the previous node ")
            
            number_need_to_actualize = (current_node - 1) - self.number_of_nodes
            
            # now all skipped nodes are made transparent as they are dumby placeholders
            for x_dalta in range(number_need_to_actualize):
                
                print(f"Creating skipped node {self.number_of_nodes + 1}-")
                # the objects for the skipped nodes will be created but made transparent
                temp_sphere = sphere(pos = vec(0,0,0))
                temp_sphere.opacity = 0
                
                temp_label = vp.label(pos = vec(0, 0, 0), text = f"{self.number_of_nodes + 1}", xoffset = 5, yoffset = 10, space = 1, 
                        height = 16, border = 4, font = 'monospace', box = False, opacity = 0, color = 1/255 * vec(255,150,0))
                temp_label.visible = False
                
                self.list_of_spheres.append(temp_sphere)
                self.list_of_labels.append(temp_label)
                self.list_of_nodes.append(vec(0, 0, 0)) # a skipped nodes position will default to zero
                                
                self.list_of_force.append(0) # leave a placeholder in the list for the node's force
                self.list_of_angle.append(0) # leave a placeholder in the list for the node's angle
                self.list_of_force_final.append(vec(0,0,0))
                print(f"act here again {len(self.list_of_force_final)}")
                
                self.list_of_force_arrows.append(vp.arrow(pos = vec(0,0,0), axis = vec(0,0,0), color = 1/255 * vec(236, 215, 16), opacity = 0))
          
                self.number_of_nodes += 1
                print(f"Skipped node {self.number_of_nodes} created successfully-")
            
            # now we can created the desired node
            print(f"Creating node {current_node}-")
            self.list_of_spheres.append(sphere(pos = vec(x, y, 0))) 
            self.list_of_labels.append(vp.label(pos = vec(x, y, 0), text = f"{current_node}", xoffset = 5, yoffset = 10, space = 1, 
                    height = 16, border = 4, font = 'monospace', box = False, opacity = 0, color = 1/255 * vec(255,150,0)))
            self.list_of_nodes.append(vec(x, y, 0))
            
            # Very important that the assicoted force to a node is created here, as the force creation method relies on the results here
            self.list_of_force.append(0) # leave a placeholder in the list for the node's force
            self.list_of_angle.append(0) # leave a placeholder in the list for the node's angle
            self.list_of_force_final.append(vec(0,0,0))
            print(f"act heree {len(self.list_of_force_final)}")
            self.list_of_force_arrows.append(vp.arrow(pos = vec(0,0,0,), axis = vec(0,0,0), color = 1/255 * vec(236, 215, 16), opacity = 0))
    
            self.number_of_nodes += 1
            print(f"Node {current_node} created successfully-")
        
        # node exist and just needs to be update the sphere and label location
        else: 
            print(f"Updating node {current_node}-")
            self.list_of_nodes[current_node - 1] = vec(x, y, 0) # update position data
            self.list_of_labels[current_node - 1].pos = vec(x, y, 0) # update position of label
            self.list_of_spheres[current_node - 1].pos = vec(x, y, 0) # update position of sphere
            
            # if a skipped node then make its objects opacqic
            self.list_of_labels[current_node - 1].visible = True 
            self.list_of_spheres[current_node - 1].opacity = 1 
            print(f"Node {current_node} updated successfully-")
               
        return vec(x, y, 0) # a return is not really needed atm but keeping in case
    
    def node_creation_with_force(self, x, y, number_of_node, force, angle): # to handle new nodes and existing node, with new or existing with forces
        
        # Node is completely new with new force, doesn't exist in list of nodes, need to create both
        if number_of_node > self.number_of_nodes: 
            self.node_creation(x, y, number_of_node)
            self.force_creation(number_of_node, force, angle) # this requires a node to exist first, then force uses the template created 
            # so new node with new force, use this one when enabling the sym. from the forces
            print("New baby node has been born")
            
        # Existing node (MOST OF THE TIME but now adding a force) maybe no position changed or yes, update the sphere and label location or/and updating forces loaction
        else: 
            # if same position
            if self.list_of_nodes[number_of_node - 1] == vec(x, y, 0):     
                         
                # if force does not exist, then replace the placeholder zeroes with actual arrow
                if self.list_of_force[number_of_node - 1] == 0 and self.list_of_angle[number_of_node - 1] == 0:
                    print("SAME POSITION AND CREATE FORCE")
                    print(f"Creating force for node-")
                    self.force_creation(number_of_node, force, angle)
                
                # if same force, then do nothing
                elif self.list_of_force[number_of_node - 1] == force and self.list_of_angle[number_of_node - 1] == angle:
                     print("SAME POSITOIN AND SAME FORCE")
                     print("No changes made-")             
                 
                # if diff force, just update force with new angles and stuff
                elif self.list_of_force[number_of_node - 1] != force or self.list_of_angle[number_of_node - 1] != angle:
                    print("SAME POSITION BUT UPDATE FORCE")
                    print("Updating force-")
                    self.force_update(number_of_node, force, angle)
                    
                # if for some reason everything else fails... do this...                
                else:
                    print("cry")
           
            # if diff position           
            else:  
                print("Updating node position-")
                self.list_of_nodes[number_of_node - 1] = vec(x, y, 0) # update position data, might need to do more
            
                self.list_of_labels[number_of_node - 1].pos = vec(x, y, 0) # update position of label
            
                self.list_of_spheres[number_of_node - 1].pos = vec(x, y, 0) # update position of sphere
                print("Node position updated successfully-")
                
                # if force does not exist, then replace the placeholder zeroes with actual arrow
                if self.list_of_force[number_of_node - 1] == 0 and self.list_of_angle[number_of_node - 1] == 0:
                    print("DIFF POSITION AND CREATE FORCE")
                    print(f"Creating force for node-")
                    self.force_creation(number_of_node, force, angle)
                
                # if same force, then just need to update the location of the force
                elif self.list_of_force[number_of_node - 1] == force and self.list_of_angle[number_of_node - 1] == angle:
                     print("DIFF POSITION BUT SAME FORCE")
                     print("Updating force-")
                     self.force_update(number_of_node, force, angle)
                
                # if diff force, just update force with new angles and stuff
                elif self.list_of_force[number_of_node - 1] != force or self.list_of_angle[number_of_node - 1] != angle:
                    print("DIFF POSITION AND DIFF FORCE")
                    print("Updating force-")
                    self.force_update(number_of_node, force, angle)
                
                # again if for some reason everything else fails... do this...
                else:
                    print("cry harder") # use this location to debug

        return vec(x, y, 0)
     
    def force_creation(self, node_on_which_current_force_acts, force_applied, angles): # to create a force arrow and format for matrix
        
        node_location = self.list_of_nodes[node_on_which_current_force_acts - 1]
 
        self.list_of_force[node_on_which_current_force_acts - 1] = force_applied
        self.list_of_angle[node_on_which_current_force_acts - 1] = angles
        
        angle = radians(angles)

        # if numbers are weird in the future try adjusting them here
        force_x = force_applied * cos(angle)
        if abs(force_x) < 0.1000:
            force_x = 0
        
        force_y = force_applied * sin(angle)
        if abs(force_y) < 0.1000:
            force_y = 0
        
        position = vec(force_x, force_y, 0)
        
        offset_from_tail = node_location + hat(position)
        
        self.list_of_force_arrows[node_on_which_current_force_acts - 1].opacity = 0.75 # reveal the force arrow 
        self.list_of_force_arrows[node_on_which_current_force_acts -1].pos = offset_from_tail
        self.list_of_force_arrows[node_on_which_current_force_acts -1].axis = node_location - offset_from_tail
               
        self.list_of_force_final[node_on_which_current_force_acts - 1] = position
        print(f"test creation 2 {len(self.list_of_force_final)}")
        
        print(f"Force created successfully-")

    def force_update(self, node_on_which_current_force_acts, force_applied, angles): # just update the force with new position and direction
      
        node_location = self.list_of_nodes[node_on_which_current_force_acts - 1]

        self.list_of_force[node_on_which_current_force_acts - 1] = force_applied
        self.list_of_angle[node_on_which_current_force_acts - 1] = angles
        
        angle = radians(angles)

        force_x = force_applied * cos(angle)
        if abs(force_x) < 0.1000:
            force_x = 0
        
        force_y = force_applied * sin(angle)
        if abs(force_y) < 0.1000:
            force_y = 0
        
        position = vec(force_x, force_y, 0)
        
        offset_from_tail = node_location + hat(position)
        
        self.list_of_force_arrows[node_on_which_current_force_acts -1].pos = offset_from_tail
        self.list_of_force_arrows[node_on_which_current_force_acts -1].axis = node_location - offset_from_tail
        
        self.list_of_force_final[node_on_which_current_force_acts - 1] = position
        
        print(f"test update {len(self.list_of_force_final)}")
        
        print("Force updated successfully-")
    
    def calculate_number_of_equations(self): # Needed for correct matrix position
        self.number_of_equations = 2 * self.number_of_nodes # Total number of equations based on number of nodes, now 3 nodes, assume clean data
        print(f"Total number of equations are {self.number_of_equations}")
        print("Formulating Known Forces Matrix-")
        self.calculate_known_forces_matrix()
        print("Successfully formulated Known Forces Matrix-")
        print(self.known_forces)
        
    def calculate_known_forces_matrix(self):
        self.known_forces = np.zeros( (self.number_of_equations, 1) )

        print(f"test calc {self.list_of_force_final}")

        i = 1
        # Filling in the known forces matrix
        for force in self.list_of_force_final:
            print(f"In list {i} the force is {force} location in martix is {i*2 - 2}")
            self.known_forces[i * 2 - 2][0] = 1 * force.x
            self.known_forces[i * 2 - 1][0] = 1 * force.y # The y transformion for the force on the element AB from A
            i += 1
            
            #print(self.known_forces)
           
    def element_creation(self, node_number_1, node_number_2): # Method to connect the two choosen nodes and generates Force vector for the element        

        # Check to flip the inputs
        if node_number_1 > node_number_2:
            temp_number = node_number_2
            node_number_2 = node_number_1
            node_number_1 = temp_number
        
        # Get the nodes (basicaly positions) from the nodes list 
        node_temp_n = self.list_of_nodes[node_number_1 - 1] # The first element of the nodes list
        node_temp_p = self.list_of_nodes[node_number_2 - 1] # The second element of the nodes list

        print(f"node {node_number_1} has loaction {node_temp_n}\n"
              + f"node {node_number_2} has location {node_temp_p}")
        
        # Create visual of element
        element_AB_visual = cylinder(pos = node_temp_n, axis = node_temp_p - node_temp_n)
        element_AB_visual.texture = vp.textures.metal
        
        temp_label = vp.label(pos = 1/2 * (element_AB_visual.axis) + element_AB_visual.pos, 
                text = f"<b>{self.number_of_current_members + 1}</b>", xoffset = 0, yoffset = 0, space = 0, height = 15, 
                border = 1, font = 'monospace', box = True, opacity = 0, linecolor = vec(0,0,0), 
                color = 1/255 * vec(255, 0, 125))
        
        self.list_of_elements_label.append(temp_label)
        self.element_visual_list.append(element_AB_visual)
        self.list_of_unknowns.append(self.number_of_current_members) # Gets number of forces aka memebers
        
        x = node_temp_p.x - node_temp_n.x # As a vector component x
        y = node_temp_p.y - node_temp_n.y # As a vector component y
        c = sqrt(x**2 + y**2)   # Mag of triangle

        element_AB = np.zeros( (self.number_of_equations, 1) ) # Creates an empty matrix where num of eqs is the number of rows, 1 is colum

        # Since node n and node p were choosen then in the element np, the force applied there
        element_AB[node_number_1 * 2 - 2][0] = x/c # The x transformion for the force on the element AB from A
        element_AB[node_number_1 * 2 - 1][0] = y/c # The y transformion for the force on the element AB from A
        element_AB[node_number_2 * 2 - 2][0] = -1 * x/c # The x transformion for the force on the element AB from B
        element_AB[node_number_2 * 2 - 1][0] = -1 * y/c # The y transformion for the force on the element AB from B

        self.list_of_elements.append(element_AB) # holds column matrix

        self.number_of_current_members += 1
        
        print("------------")
        print(f"Successfully created element {self.number_of_current_members} -")
        
    def element_update(self, current_element, node_number_1, node_number_2): # Method to connect the two choosen nodes and generates Force vector for the element        

        # Check to flip the inputs
        if node_number_1 > node_number_2:
            temp_number = node_number_2
            node_number_2 = node_number_1
            node_number_1 = temp_number
        
        # Get the nodes (basicaly positions) from the nodes list 
        node_temp_n = self.list_of_nodes[node_number_1 - 1] # The first element of the nodes list
        node_temp_p = self.list_of_nodes[node_number_2 - 1] # The second element of the nodes list

        print(f"node {node_number_1} has loaction {node_temp_n}\n"
              + f"node {node_number_2} has location {node_temp_p}")
        
        # Update visual of element       
        b = self.element_visual_list[current_element - 1].pos = node_temp_n
        a = self.element_visual_list[current_element - 1].axis = node_temp_p - node_temp_n
        self.element_visual_list[current_element - 1].opacity = 1
        
        self.list_of_elements_label[current_element - 1].pos = 1/2 * a + b
        self.list_of_elements_label[current_element - 1].visible = True # useful for future empty list detection
        
        x = node_temp_p.x - node_temp_n.x # As a vector component x
        y = node_temp_p.y - node_temp_n.y # As a vector component y
        c = sqrt(x**2 + y**2)   # Mag of triangle

        element_AB = np.zeros( (self.number_of_equations, 1) ) # Creates an empty matrix where num of eqs is the number of rows, 1 is colum

        # Since node n and node p were choosen then in the element np, the force applied there
        element_AB[node_number_1 * 2 - 2][0] = x/c # The x transformion for the force on the element AB from A
        element_AB[node_number_1 * 2 - 1][0] = y/c # The y transformion for the force on the element AB from A
        element_AB[node_number_2 * 2 - 2][0] = -1 * x/c # The x transformion for the force on the element AB from B
        element_AB[node_number_2 * 2 - 1][0] = -1 * y/c # The y transformion for the force on the element AB from B

        # needs more testing 
        self.list_of_elements[current_element - 1] = element_AB # holds column matrix, replaces previous 
        
        print("------------")
        print(f"Updated element {self.number_of_current_members} successfully-")
    
    def element_check(self, current_element, node_number_1, node_number_2):
        print(f"{self.number_of_current_members} element(s) in backend vs current element {current_element}")
        
        # Check to see if completely new element has to be created with no element skips
        if current_element > self.number_of_current_members and current_element - 1 == self.number_of_current_members: 
            print(f"Creating element {current_element}")
            self.element_creation(node_number_1, node_number_2) # if so then just create the element
        
        # Here we are skipping a few elements in the line to create the new element, so we need to actualize the skipped
        elif current_element > self.number_of_current_members and current_element - 1 != self.number_of_current_members:
            print("Trying to actualize an element without actualizing the previous element(s)")
            
            number_need_to_actualize = (current_element - 1) - self.number_of_current_members # math was done to figure out number
            
            # All skipped elements will be create as transparent dumby placeholders
            for x_dalta in range(number_need_to_actualize):
                print(f"Creating skipped element {self.number_of_current_members + 1}")
            
                # for dumby element just default to picking the first two nodes in the list
                self.element_creation(1,2) # if the first two nodes don't exist then think of something else
                
                # then change the opacity of these dumby elements
                self.element_visual_list[self.number_of_current_members - 1].opacity = 0
                self.list_of_elements_label[self.number_of_current_members - 1].visible = False
            
            # Now created desired element  
            print(f"Creating element {current_element}")  
            self.element_creation(node_number_1, node_number_2)
            print("Complex operation conducted successfully")
        
        # Just update the element with new nodes 
        else:
            print(f"Updating element {current_element}-")
            self.element_update(current_element, node_number_1, node_number_2)
 
    def roller_creation(self, node_number, number):
        
        node_roller_reaction = self.list_of_nodes[node_number - 1]
        roller_support = vp.sphere(pos = node_roller_reaction - vec(0 , 0.1 + 0.1, 0), radius=0.1,
                                texture = vp.textures.granite)

        # Since node n and node p were choosen then in the element np, the force applied there
        roller_reactions = np.zeros( (self.number_of_equations, 1) ) # Creates an empty matrix where num of eqs is the number of rows, 1 is colum
        roller_reactions[node_number * 2 - 1][0] = 1 # The x transformion for the force on pin 
        
        ground = vp.box(pos = roller_support.pos - vec(0, roller_support.radius + 0.5, 0), 
                        size = vec(1, 1 ,1), texture = vp.textures.wood)

        self.list_of_visual_rollers.append(roller_support)
        self.list_of_rollers.append(roller_reactions)
        self.list_of_rollers_ground.append(ground)
        
        print(roller_reactions)
             
        self.number_of_backend_rollers += 1
  
        print(f"Successfully created roller {number} -")
        print("------------")
        
    def roller_update(self, node_number, number):
        
        node_roller_reaction = self.list_of_nodes[node_number - 1]
        q = self.list_of_visual_rollers[number - 1].pos = node_roller_reaction - vec(0 , 0.1 + 0.1, 0)
        self.list_of_visual_rollers[number - 1].opacity = 1

        # Since node n and node p were choosen then in the element np, the force applied there
        roller_reactions = np.zeros( (self.number_of_equations, 1) ) # Creates an empty matrix where num of eqs is the number of rows, 1 is colum
        roller_reactions[node_number * 2 - 1][0] = 1 # The x transformion for the force on pin 
        
        self.list_of_rollers_ground[number - 1].pos = q - vec(0, self.list_of_visual_rollers[number - 1].radius + 0.5, 0)
        self.list_of_rollers_ground[number - 1].opacity = 1
                       
        # just stright up overwrite the old one
        self.list_of_rollers[number - 1] = roller_reactions 
        print(roller_reactions)
        
        print(f"Successfully updated roller {number} -")
        print("------------")
                 
    def roller_check(self, node_number, current_number):
     
        print(f"{self.number_of_backend_rollers} roller(s) in backend vs current roller {current_number}")
        
        # Check to see if completely new roller has to be created with no roller skips
        if current_number > self.number_of_backend_rollers and current_number - 1 == self.number_of_backend_rollers: 
            print(f"Creating roller {current_number} -")
            self.roller_creation(node_number, current_number) # if so then just create the roller
        
        # Here we are skipping a few rollers in the line to create the new roller, so we need to actualize the skipped
        elif current_number > self.number_of_backend_rollers and current_number - 1 != self.number_of_backend_rollers:
            print("Trying to actualize an roller without actualizing the previous roller(s)")
            
            number_need_to_actualize = (current_number - 1) - self.number_of_backend_rollers # math was done to figure out number
            
            # All skipped rollers will be create as transparent dumby placeholders
            for x_dalta in range(number_need_to_actualize):
                print(f"Creating skipped roller {self.number_of_backend_rollers + 1}")
            
                # for dumby rollers just default to picking the first node and row number 1
                self.roller_creation(1, self.number_of_backend_rollers + 1) # if the first node don't exist then think of something else
                
                # then change the opacity of these dumby rollers
                self.list_of_visual_rollers[self.number_of_backend_rollers - 1].opacity = 0
                self.list_of_rollers_ground[self.number_of_backend_rollers - 1].opacity = 0
            
            # Now created desired roller  
            print(f"Creating roller {current_number} -")  
            self.roller_creation(node_number, current_number)
            print("Complex operation conducted successfully")
        
        # Just update the roller with new node 
        else:
            print(f"Updating roller {current_number} -")
            self.roller_update(node_number, current_number)

    def pin_creation(self, node_number, number):
        
        node_pin_reaction = self.list_of_nodes[node_number - 1]
        
        pin_reactions1 = np.zeros( (self.number_of_equations, 1) ) # Creates an empty matrix where num of eqs is the number of rows, 1 is colum
        pin_reactions1[node_number * 2 - 2][0] = 1 # The x transformion for the force on pin

        pin_reactions2 = np.zeros( (self.number_of_equations, 1) ) # Creates an empty matrix where num of eqs is the number of rows, 1 is colum
        pin_reactions2[node_number * 2 - 1][0] = 1 # The y transformion for the force on pin
     
        # more work to be done at matrix ++++++++++++++++++++++++++++++++
        pin_reactions = np.hstack((pin_reactions1, pin_reactions2))
     
        print(f"pin reaction \n {pin_reactions}")
     
        # needed to find correct spacing 
        pin_supportR = vp.sphere(pos = node_pin_reaction - vec(0 , 0.1 + 0.1, 0), radius=0.1,
                                texture = vp.textures.granite, opacity = 0)
     
        ground = vp.box(pos = pin_supportR.pos - vec(0, pin_supportR.radius + 0.5, 0), 
                        size = vec(1, 1 ,1), texture = vp.textures.wood)

        pin_support = vp.pyramid(pos = vec(node_pin_reaction.x, ground.pos.y + 0.05, 0), 
                         size = vec(node_pin_reaction.y - ground.pos.y , 0.5, 0.5),
                         axis = vec(0, 1, 0), texture = vp.textures.granite)
        
        self.list_of_pins.append(pin_reactions)
        self.list_of_pins_spacing.append(pin_supportR)
        self.list_of_pins_ground.append(ground)
        self.list_of_visual_pins.append(pin_support)
                 
                  
        self.number_of_backend_pins += 1
  
        print(f"Successfully created pin {number} -")
        print("------------")

    def pin_update(self, node_number, number):
        
        node_pin_reaction = self.list_of_nodes[node_number - 1]
        
        pin_reactions1 = np.zeros( (self.number_of_equations, 1) ) # Creates an empty matrix where num of eqs is the number of rows, 1 is colum
        pin_reactions1[node_number * 2 - 2][0] = 1 # The x transformion for the force on pin

        pin_reactions2 = np.zeros( (self.number_of_equations, 1) ) # Creates an empty matrix where num of eqs is the number of rows, 1 is colum
        pin_reactions2[node_number * 2 - 1][0] = 1 # The y transformion for the force on pin
     
        # more work to be done at matrix ++++++++++++++++++++++++++++++++
        pin_reactions = np.hstack((pin_reactions1, pin_reactions2))
     
        self.list_of_pins[number - 1] = pin_reactions
        print(f"pin reaction \n {pin_reactions}")
     
        # needed to find correct spacing 
        s = self.list_of_pins_spacing[number - 1].pos = node_pin_reaction - vec(0 , 0.1 + 0.1, 0)
     
        g = self.list_of_pins_ground[number - 1].pos = s.pos - vec(0, s.radius + 0.5, 0)
        self.list_of_pins_ground[number - 1].opacity = 1
     
        self.list_of_visual_pins[number - 1].pos = vec(node_pin_reaction.x, g.pos.y + 0.05, 0)
        self.list_of_visual_pins[number - 1].opacity = 1
 
        print(f"Successfully updated pin {number} -")
        print("------------")

    def pin_check(self, node_number, current_number):
     
        print(f"{self.number_of_backend_pins} pin(s) in backend vs current pin {current_number}")
        
        # Check to see if completely new pin has to be created with no pin skips
        if current_number > self.number_of_backend_pins and current_number - 1 == self.number_of_backend_pins: 
            print(f"Creating pin {current_number} -")
            self.pin_creation(node_number, current_number)
        
        # Here we are skipping a few pins in the line to create the new pin, so we need to actualize the skipped
        elif current_number > self.number_of_backend_pins and current_number - 1 != self.number_of_backend_pins:
            print("Trying to actualize an pin without actualizing the previous pin(s)")
            
            number_need_to_actualize = (current_number - 1) - self.number_of_backend_pins # math was done to figure out number
            
            # All skipped pins will be create as transparent dumby placeholders
            for x_dalta in range(number_need_to_actualize):
                print(f"Creating skipped pin {self.number_of_backend_pins + 1}")
            
                # for dumby pins just default to picking the first node and row number 1
                self.pin_creation(1, self.number_of_backend_pins + 1) # if the first node don't exist then think of something else
                
                # then change the opacity of these dumby pins
                self.list_of_visual_pins[self.number_of_backend_pins - 1].opacity = 0
                self.list_of_pins_ground[self.number_of_backend_pins - 1].opacity = 0
            
            # Now created desired roller  
            print(f"Creating pin {current_number} -")  
            self.pin_creation(node_number, current_number)
            print("Complex operation conducted successfully")
        
        # Just update the pin with new node 
        else:
            print(f"Updating pin {current_number} -")
            self.pin_update(node_number, current_number)
                 
    def create_Master_Matrix(self):
        print("Formulating Master Matrix-")
        
        self.master_matrix = np.concatenate((self.list_of_elements[0], self.list_of_elements[1]), axis = 1)
        for x in arange(0, len(self.list_of_elements) - 2, 1):
            self.master_matrix = np.hstack((self.master_matrix, self.list_of_elements[x + 2]))
            
        print("Sucessfully formulated Master Matrix-")
        print(self.master_matrix)
        
    def create_Engineering_Support_Matrix(self):
        print("Formulating Engineering Support Matrix-")
        
        if len(self.list_of_rollers) > 1:
            self.roller_matrix = np.concatenate((self.list_of_rollers[0], self.list_of_rollers[1]), axis = 1)
            for x in arange(0, len(self.list_of_rollers) - 2, 1):
                self.roller_matrix = np.hstack((self.roller_matrix, self.list_of_rollers[x + 2]))
                
        elif len(self.list_of_rollers)  == 1:
            self.roller_matrix = self.list_of_rollers[0]

        if len(self.list_of_pins) > 1:
            self.pin_matrix = np.concatenate((self.list_of_pins[0], self.list_of_pins[1]), axis = 1)
            for x in arange(0, len(self.list_of_pins) - 2, 1):
                self.pin_matrix = np.hstack((self.pin_matrix, self.list_of_pins[x + 2]))
                
        elif len(self.list_of_pins)  == 1:
            self.pin_matrix = self.list_of_pins[0]
  
        type(self.roller_matrix)
  
        if type(self.roller_matrix) == type(int):
            print("case ")
            self.engineering_support_matrix = self.pin_matrix
            
        elif type(self.pin_matrix) == type(int):
            self.engineering_support_matrix = self.roller_matrix
            
        else:
            self.engineering_support_matrix = np.concatenate((self.roller_matrix, self.pin_matrix), axis = 1)
            
        print(self.engineering_support_matrix)
        print("Sucessfully formulated Engineering Support Matrix-")
        
    def solve_matrix(self):
        self.create_Master_Matrix()
        self.create_Engineering_Support_Matrix()
        # can do this later with a list of supports      
        #self.coeffeicent_matrix = np.hstack((self.master_matrix, self.roller_matrix))
        self.coeffeicent_matrix = np.concatenate((self.master_matrix, self.engineering_support_matrix), axis = 1)
        print(self.coeffeicent_matrix)
        
        print("Solution Matrix")
        self.unknown_forces = (np.linalg.inv(self.coeffeicent_matrix)).dot(self.known_forces)  
        print(self.unknown_forces)
        print("===========================================") 
        
        self.solution_postprocessing()
        
    def solution_postprocessing(self):
        max_pos_force = np.amax(self.unknown_forces)
        max_neg_force = np.amin(self.unknown_forces)

        for x in arange(0, np.size(self.unknown_forces) - 3, 1):
            force = self.unknown_forces[x][0]
            force_abs = abs(self.unknown_forces[x][0])
            
            if  force > 0 and force > 0.000001:
                self.element_visual_list[x].color = force/max_pos_force * vec(0.8, 0, 0)
                print(f'Element {x + 1} has a force of {force_abs:.2f} and is in tension.')
            elif force < 0 and force < -0.000001:
                self.element_visual_list[x].color = force/max_neg_force * vec(0, 0, 0.8)
                print(f'Element {x + 1} has a force of {force_abs:.2f} and is in compression.')
            else:
                print(f'Element {x + 1} is a zero force memeber.')

        text_1 = vp.wtext(text = "Blue elements mean in compression\n")

        text_2 = vp.wtext(text = "Red elements mean in tension")
