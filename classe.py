import pygame
import copy
pygame.init()
def affichage_pion(surface):
   liste_pion=[]
   liste_pion_w=[]
   d=0
   for e in range(8):
       pione=pion(d,50,50,50,surface,image="chess/bP.png")
       d+=50
       liste_pion.append(pione)
   d=0
   for e in range(8):
       pione=pion(d,300,50,50,surface,image="chess/wp.png",color="white")
       d+=50
       liste_pion.append(pione)
   my_queen=queen(150,0,50,50,surface,image="chess/bQ.png")
   my_cavalier=cavalier(50,0,50,50,surface,image="chess/bKN.png")
   my_cavalier2=cavalier(300,0,50,50,surface,image="chess/bKN.png")
   my_fou=fou(100,0,50,50,surface,image="chess/bB.png")
   my_fou2=fou(250,0,50,50,surface,image="chess/bB.png")
   my_garde=garde(0,0,50,50,surface,image="chess/bR.png")
   my_garde2=garde(350,0,50,50,surface,image="chess/bR.png")
   my_king=king(200,0,50,50,surface,image="chess/bK.png")
   liste_pion.append(my_queen)
   liste_pion.append(my_fou)
   liste_pion.append(my_garde)
   liste_pion.append(my_king)
   liste_pion.append(my_cavalier)
   liste_pion.append(my_cavalier2)
   liste_pion.append(my_fou2)
   liste_pion.append(my_garde2)
   my_queen_w=queen(150,350,50,50,surface,image="chess/wQ.png",color="white")
   my_cavalier_w=cavalier(50,350,50,50,surface,image="chess/wKN.png",color="white")
   my_cavalier2_w=cavalier(300,350,50,50,surface,image="chess/wKN.png",color="white")
   my_fou_w=fou(100,350,50,50,surface,image="chess/wB.png",color="white")
   my_fou2_w=fou(250,350,50,50,surface,image="chess/wB.png",color="white")
   my_garde_w=garde(0,350,50,50,surface,image="chess/wR.png",color="white")
   my_garde2_w=garde(350,350,50,50,surface,image="chess/wR.png",color="white")
   my_king_w=king(200,350,50,50,surface,image="chess/wK.png",color="white")
   liste_pion.append(my_queen_w)
   liste_pion.append(my_fou_w)
   liste_pion.append(my_garde_w)
   liste_pion.append(my_king_w)
   liste_pion.append(my_cavalier_w)
   liste_pion.append(my_cavalier2_w)
   liste_pion.append(my_fou2_w)
   liste_pion.append(my_garde2_w)
   return liste_pion[:]
def affichage_carro(surface):
   white=[243,245,209]
   black=[164,184,162]
   len_listecase=0
   cordyx_case=[0,0]
   N_case_x=0
   N_case_y=0
   liste_case=[]
   patern=0
   for e in range(32):
      if len_listecase==8:
         cordyx_case[1]+=50
         N_case_y+=1
         cordyx_case[0]=0
         N_case_x=0
         len_listecase=0
         if patern==0:
            patern=1
         else:
            patern=0
      if patern==0:
         case_1=case(cordyx_case[0],cordyx_case[1],50,50,color=white)
         pygame.draw.rect(surface,white,case_1)
         liste_case.append(case_1)
         N_case_x+=1
         cordyx_case[0]+=50
         case_2=case(cordyx_case[0],cordyx_case[1],50,50,color=black)
         pygame.draw.rect(surface,black,case_2)
         liste_case.append(case_2)
         N_case_x+=1
         cordyx_case[0]+=50
      else:
         case_2=case(cordyx_case[0],cordyx_case[1],50,50,color=black)
         pygame.draw.rect(surface,black,case_2)
         liste_case.append(case_2)
         cordyx_case[0]+=50
         N_case_x+=1
         case_1=case(cordyx_case[0],cordyx_case[1],50,50,color=white)
         pygame.draw.rect(surface,white,case_1)
         liste_case.append(case_1)
         cordyx_case[0]+=50
         N_case_x+=1

      len_listecase+=2

      pygame.display.flip()
   return liste_case[:]
def fonction(dico):
   liste_cle=[]
   for e in dico:
      liste_cle.append(e)
   return liste_cle
class case(pygame.Rect):
   case_carro=[]
   def  __init__(self,left,top,width,height,color=[0,0,0]):
      pygame.Rect.__init__(self,left,top,width,height)
      try:
            NcaseX=int(self.x/50)
            NcaseY=int(self.y/50)
      except ZeroDivisionError:
            NcaseX=0
            NcaseY=0
      self.NcaseX=NcaseX
      self.NcaseY=NcaseY
      self.num_case={NcaseX:self.x,str(NcaseY):self.y}
      self.color=color
      case.case_carro.append(self.num_case)
class show_case_neg(case):
   def __init__(self,left,top,width,height,NcaseX=None,NcaseY=None,color=[63,50,255]):
      case.__init__(self,left,top,width,height,NcaseX,NcaseY,color)
class pion(case):
   num_pion=1
   def __init__(self,left,top,width,height,surface,image,color="black"):
      case.__init__(self,left,top,width,height)
      self.pion=pygame.image.load(image)
      self.pion.convert()
      self.color=color
      NcaseX=0
      NcaseY=0
      try:
         NcaseX=int(self.x/50)
         NcaseY=int(self.y/50)
      except ZeroDivisionError:
         NcaseX=0
         NcaseY=0
      self.info_move=False
      self.NcaseX=NcaseX
      self.NcaseY=NcaseY
      self.case_pion={self.NcaseX:self.x,str(self.NcaseY):self.y}
      self.pion.set_colorkey([255,255,255])
      self.pion=pygame.transform.scale(self.pion,[50,50])
      surface.blit(self.pion,[self.case_pion[self.NcaseX],self.case_pion[str(self.NcaseY)]])
      self.num_pion=pion.num_pion
      self.premier_coup=True
      pion.num_pion+=1
   def show_move(self,surface,liste_case,liste_pion):
         self.info_move=True
         black_white=self.color=="black"
         hypx=self.NcaseX
         hypy=self.NcaseY
         dernier_move=[]
         liste2=[]
         pion_sur_pion=True
         if black_white:
            hypy+=1
            if self.premier_coup:
               liste2=[hypx,str(hypy+1)]
               
         else:
            hypy-=1
            if self.premier_coup:
               liste2=[hypx,str(hypy-1)]
         hyp_case_pion={hypx:self.x,str(hypy):self.y}
         liste1=fonction(hyp_case_pion)
         for e in liste_case:
            #print(liste1[:],liste2[:],"L0")
            if liste1[:]==fonction(e.num_case):
               for a in liste_pion:
                  if liste1[:] == fonction(a.case_pion):
                     pion_sur_pion=False
               if pion_sur_pion:
                  rect_hyp=case(e.x,e.y,50,50,color=[53,60,255])
                  pygame.draw.rect(surface,[53,60,255],rect_hyp,)
                  dernier_move.append(rect_hyp)
                  case_trouver=True
            else:
               if liste2[:]==fonction(e.num_case):
                  for a in liste_pion:
                     if liste2[:] == fonction(a.case_pion):
                        pion_sur_pion=False
                  if pion_sur_pion:
                     rect_hyp=case(e.x,e.y,50,50,color=[53,60,255])
                     pygame.draw.rect(surface,[53,60,255],rect_hyp,)
                     dernier_move.append(rect_hyp)
                     case_trouver=True
            

         
         liste1[0]-=1
         for e in liste_case:
            #print(liste1[:],liste2[:],"L2")
            liste2=fonction(e.num_case)
            if liste1[:]==liste2[:]:
               for a in liste_pion:
                  if fonction(a.case_pion) == liste1[:] and a.color != self.color:
                     rect_hyp_kills=case(e.x,e.y,50,50,color=[80,80,80])
                     pygame.draw.rect(surface,[80,80,80],rect_hyp_kills)
                     
                     dernier_move.append(rect_hyp_kills)
         hypx+=2
         hyp_case_pion={hypx:self.x,str(hypy):self.y}
         liste1[0]+=2
         for e in liste_case:
            liste2=fonction(e.num_case)
            #print(liste1[:],liste2[:],"L1")
            if liste1[:]==liste2[:]:
               for a in liste_pion:
                  if fonction(a.case_pion) == liste1[:] and self.color!= a.color:
                     rect_hyp_kill=case(e.x,e.y,50,50,color=[80,80,80])
                     pygame.draw.rect(surface,[80,80,80],rect_hyp_kill)
                     dernier_move.append(rect_hyp_kill)

                     


         return dernier_move[:]



   def move(self,surface,liste_case,liste_pion,coordyx):
      #zone=fonction(coordyx.num_case)
      if self.premier_coup:
         self.premier_coup=False
      self.y,self.x=coordyx.y,coordyx.x
      self.NcaseY,self.NcaseX=int(coordyx.y/50),int(coordyx.x/50)#self.dernier_move[len(self.dernier_move)-1].y,self.dernier_move[len(self.dernier_move)-1].x
      self.case_pion={self.NcaseX:self.x,str(self.NcaseY):self.y}
       
      surface.fill([0,0,0])
      for e in liste_case:
         pygame.draw.rect(surface,e.color,e)

      for e in liste_pion:
         surface.blit(e.pion,[e.case_pion[e.NcaseX],e.case_pion[str(e.NcaseY)]])
   def question_kill(self,surface,liste_pion,liste_case):
      king_dead=False
      for a,c in enumerate(liste_pion):
         if c.case_pion==self.case_pion and c.num_pion!=self.num_pion:
            if type(liste_pion[a])==king:
               liste_pion[a].king_dead=True
               king_dead=True
               check=liste_pion[a]
               del liste_pion[a]
            else:
               del liste_pion[a]
      surface.fill([0,0,0])
      for e in liste_case:
         pygame.draw.rect(surface,e.color,e)

      for e in liste_pion:
         surface.blit(e.pion,[e.case_pion[e.NcaseX],e.case_pion[str(e.NcaseY)]])
      self.info_move=False
      if king_dead:
         return check
      else:
         return None
      

class queen(pion):
   def __init__(self,left,top,width,height,surface,image,color="black"):
      pion.__init__(self,left,top,width,height,surface,image,color)

   def show_move(self,surface,liste_case,liste_pion):
      liste1=[self.NcaseX,str(self.NcaseY+1)]
      liste2=[self.NcaseX+1,str(self.NcaseY)]
      liste3=[self.NcaseX-1,str(self.NcaseY)]
      liste4=[self.NcaseX,str(self.NcaseY-1)]
      diago1=[self.NcaseX-1,str(self.NcaseY+1)]
      diago2=[self.NcaseX+1,str(self.NcaseY-1)]
      diago3=[self.NcaseX+1,str(self.NcaseY+1)]
      diago4=[self.NcaseX-1,str(self.NcaseY-1)]

      liste_case_pre=[]
      tempo=[0,0]

      Gigaliste=[liste1[:],liste2[:],liste3[:],liste4[:],diago1[:],diago2[:],diago3[:],diago4[:]]
      dernier_move=[]
      case_good=True
      gigalist2=[]
      diag1=True
      diag2=True
      case_good=True
      for o in range(8):
         for i in liste_case:
            if diago3==fonction(i.num_case):
               for pion in liste_pion:
                     if fonction(pion.case_pion) ==diago3 and pion.color==self.color:
                        case_good=False
               if case_good:                          
                  rect_queen=case(i.x,i.y,50,50,surface)
                  pygame.draw.rect(surface,[53,60,255],rect_queen)
                  dernier_move.append(rect_queen)
                  for pion in liste_pion:
                     if fonction(pion.case_pion) ==diago3:
                           case_good=False
                  tempo=diago3
                  tempo[0]+=1
                  tempo[1]=int(tempo[1])
                  tempo[1]+=1
                  tempo[1]=str(tempo[1])
                  diago3=tempo[:]
      case_good=True
      for o in range(8):
         for i in liste_case:
            if diago1==fonction(i.num_case):
               for pion in liste_pion:
                     if fonction(pion.case_pion) ==diago1 and pion.color==self.color:
                        case_good=False
               if case_good:                         
                  rect_queen=case(i.x,i.y,50,50,surface)
                  pygame.draw.rect(surface,[53,60,255],rect_queen)
                  dernier_move.append(rect_queen)
                  for pion in liste_pion:
                     if fonction(pion.case_pion) ==diago1:
                           case_good=False
                  tempo=diago1
                  tempo[0]-=1
                  tempo[1]=int(tempo[1])
                  tempo[1]+=1
                  tempo[1]=str(tempo[1])
                  diago1=tempo[:]
      case_good=True
      for o in range(8):
         for i in liste_case:
            if diago2==fonction(i.num_case):
               for pion in liste_pion:
                     if fonction(pion.case_pion) ==diago2 and pion.color==self.color:
                        case_good=False
               if case_good:                         
                  rect_queen=case(i.x,i.y,50,50,surface)
                  pygame.draw.rect(surface,[53,60,255],rect_queen)
                  dernier_move.append(rect_queen)
                  for pion in liste_pion:
                     if fonction(pion.case_pion) ==diago2:
                           case_good=False
                  tempo=diago2
                  tempo[0]+=1
                  tempo[1]=int(tempo[1])
                  tempo[1]-=1
                  tempo[1]=str(tempo[1])
                  diago2=tempo[:]
      case_good=True
      for o in range(8):
         for i in liste_case:
            if diago4==fonction(i.num_case):
               for pion in liste_pion:
                     if fonction(pion.case_pion) ==diago4 and pion.color==self.color:
                        case_good=False
               if case_good:                         
                  rect_queen=case(i.x,i.y,50,50,surface)
                  pygame.draw.rect(surface,[53,60,255],rect_queen)
                  dernier_move.append(rect_queen)
                  for pion in liste_pion:
                     if fonction(pion.case_pion) ==diago4:
                           case_good=False
                  tempo=diago4
                  tempo[0]-=1
                  tempo[1]=int(tempo[1])
                  tempo[1]-=1
                  tempo[1]=str(tempo[1])
                  diago4=tempo[:]
      case_good=True
      for o in range(8):
         for i in liste_case:
            if liste1==fonction(i.num_case):
               for pion in liste_pion:
                     if fonction(pion.case_pion) ==liste1 and pion.color==self.color:
                        case_good=False
               if case_good:                          
                  rect_queen=case(i.x,i.y,50,50,surface)
                  pygame.draw.rect(surface,[53,60,255],rect_queen)
                  dernier_move.append(rect_queen)
                  for pion in liste_pion:
                     if fonction(pion.case_pion) ==liste1:
                        case_good=False
                  tempo=liste1
                  tempo[1]=int(tempo[1])
                  tempo[1]+=1
                  tempo[1]=str(tempo[1])
                  liste1=tempo[:]
                  
      case_good=True
      for o in range(8):
         for i in liste_case:
            if liste2==fonction(i.num_case):
               for pion in liste_pion:
                     if fonction(pion.case_pion) ==liste2 and pion.color==self.color:
                        case_good=False
               if case_good:                          
                  rect_queen=case(i.x,i.y,50,50,surface)
                  pygame.draw.rect(surface,[53,60,255],rect_queen)
                  dernier_move.append(rect_queen)
                  for pion in liste_pion:
                     if fonction(pion.case_pion) ==liste2:
                        case_good=False
                  tempo=liste2
                  tempo[0]+=1
                  liste2=tempo[:]
      case_good=True
      for o in range(8):
         for i in liste_case:
            if liste3==fonction(i.num_case):
               for pion in liste_pion:
                     if fonction(pion.case_pion) ==liste3 and pion.color==self.color:
                        case_good=False
               if case_good:                         
                  rect_queen=case(i.x,i.y,50,50,surface)
                  pygame.draw.rect(surface,[53,60,255],rect_queen)
                  dernier_move.append(rect_queen)
                  for pion in liste_pion:
                     if fonction(pion.case_pion) ==liste3:
                        case_good=False
                  tempo=liste3
                  tempo[0]-=1
                  liste3=tempo[:]
      case_good=True
      for o in range(8):
         for i in liste_case:
            if liste4==fonction(i.num_case):
               for pion in liste_pion:
                     if fonction(pion.case_pion) ==liste4 and pion.color==self.color:
                        case_good=False
               if case_good:                        
                  rect_queen=case(i.x,i.y,50,50,surface)
                  pygame.draw.rect(surface,[53,60,255],rect_queen)
                  dernier_move.append(rect_queen)
                  for pion in liste_pion:
                     if fonction(pion.case_pion) ==liste4:
                        case_good=False
                  tempo=liste4
                  tempo[1]=int(tempo[1])
                  tempo[1]-=1
                  tempo[1]=str(tempo[1])
                  liste4=tempo[:]
                        
      return dernier_move[:]
class fou(pion):
   def __init__(self,left,top,width,height,surface,image,color="black",):
      if color=="black":
         pass
      else:
         image="chess/wB.png"
      pion.__init__(self,left,top,width,height,surface,image,color,)
   def show_move(self,surface,liste_case,liste_pion):
      diago1=[self.NcaseX-1,str(self.NcaseY+1)]
      diago2=[self.NcaseX+1,str(self.NcaseY-1)]
      diago3=[self.NcaseX+1,str(self.NcaseY+1)]
      diago4=[self.NcaseX-1,str(self.NcaseY-1)]
      liste_case_pre=[]
      tempo=[0,0]
      dernier_move=[]
      case_good=True
      gigalist2=[]
      diag1=True
      diag2=True
      for o in range(8):
         for i in liste_case:
            if diago3==fonction(i.num_case):
               for pion in liste_pion:
                     if fonction(pion.case_pion) ==diago3 and pion.color==self.color:
                        case_good=False
               if case_good:                          
                  rect_queen=case(i.x,i.y,50,50,surface)
                  pygame.draw.rect(surface,[53,60,255],rect_queen)
                  dernier_move.append(rect_queen)
                  for pion in liste_pion:
                     if fonction(pion.case_pion) ==diago3:
                           case_good=False
                  tempo=diago3
                  tempo[0]+=1
                  tempo[1]=int(tempo[1])
                  tempo[1]+=1
                  tempo[1]=str(tempo[1])
                  diago3=tempo[:]
      case_good=True
      for o in range(8):
         for i in liste_case:
            if diago1==fonction(i.num_case):
               for pion in liste_pion:
                     if fonction(pion.case_pion) ==diago1 and pion.color==self.color:
                        case_good=False
               if case_good:                         
                  rect_queen=case(i.x,i.y,50,50,surface)
                  pygame.draw.rect(surface,[53,60,255],rect_queen)
                  dernier_move.append(rect_queen)
                  for pion in liste_pion:
                     if fonction(pion.case_pion) ==diago1:
                           case_good=False
                  tempo=diago1
                  tempo[0]-=1
                  tempo[1]=int(tempo[1])
                  tempo[1]+=1
                  tempo[1]=str(tempo[1])
                  diago1=tempo[:]
      case_good=True
      for o in range(8):
         for i in liste_case:
            if diago2==fonction(i.num_case):
               for pion in liste_pion:
                     if fonction(pion.case_pion) ==diago2 and pion.color==self.color:
                        case_good=False
               if case_good:                          
                  rect_queen=case(i.x,i.y,50,50,surface)
                  pygame.draw.rect(surface,[53,60,255],rect_queen)
                  dernier_move.append(rect_queen)
                  for pion in liste_pion:
                     if fonction(pion.case_pion) ==diago2:
                           case_good=False
                  tempo=diago2
                  tempo[0]+=1
                  tempo[1]=int(tempo[1])
                  tempo[1]-=1
                  tempo[1]=str(tempo[1])
                  diago2=tempo[:]
      case_good=True
      for o in range(8):
         for i in liste_case:
            if diago4==fonction(i.num_case):
               for pion in liste_pion:
                     if fonction(pion.case_pion) ==diago4 and pion.color==self.color:
                        case_good=False
               if case_good:                          
                  rect_queen=case(i.x,i.y,50,50,surface)
                  pygame.draw.rect(surface,[53,60,255],rect_queen)
                  dernier_move.append(rect_queen)
                  for pion in liste_pion:
                     if fonction(pion.case_pion) ==diago4:
                           case_good=False
                  tempo=diago4
                  tempo[0]-=1
                  tempo[1]=int(tempo[1])
                  tempo[1]-=1
                  tempo[1]=str(tempo[1])
                  diago4=tempo[:]
                        
      return dernier_move[:]
class garde(pion):
   def __init__(self,left,top,width,height,surface,image,color="black"):
      pion.__init__(self,left,top,width,height,surface,image,color)
   def show_move(self,surface,liste_case,liste_pion):
      liste1=[self.NcaseX,str(self.NcaseY+1)]
      liste2=[self.NcaseX+1,str(self.NcaseY)]
      liste3=[self.NcaseX-1,str(self.NcaseY)]
      liste4=[self.NcaseX,str(self.NcaseY-1)]
      tempo=[0,0]
      dernier_move=[]
      gigalist2=[]
      diag1=True
      diag2=True
      case_good=True
      for o in range(8):
         for i in liste_case:
            if liste1==fonction(i.num_case):
               for pion in liste_pion:
                     if fonction(pion.case_pion) ==liste1 and pion.color==self.color:
                        case_good=False
               if case_good:                          
                  rect_queen=case(i.x,i.y,50,50,surface)
                  pygame.draw.rect(surface,[53,60,255],rect_queen)
                  dernier_move.append(rect_queen)
                  for pion in liste_pion:
                     if fonction(pion.case_pion) ==liste1:
                        case_good=False
                  tempo=liste1
                  tempo[1]=int(tempo[1])
                  tempo[1]+=1
                  tempo[1]=str(tempo[1])
                  liste1=tempo[:]
      case_good=True
      for o in range(8):
         for i in liste_case:
            if liste2==fonction(i.num_case):
               for pion in liste_pion:
                     if fonction(pion.case_pion) ==liste2 and pion.color==self.color:
                        case_good=False
               if case_good:                       
                  rect_queen=case(i.x,i.y,50,50,surface)
                  pygame.draw.rect(surface,[53,60,255],rect_queen)
                  dernier_move.append(rect_queen)
                  for pion in liste_pion:
                     if fonction(pion.case_pion) ==liste2:
                        case_good=False
                  tempo=liste2
                  tempo[0]+=1
                  liste2=tempo[:]
      case_good=True
      for o in range(8):
         for i in liste_case:
            if liste3==fonction(i.num_case):
               for pion in liste_pion:
                     if fonction(pion.case_pion) ==liste3 and pion.color==self.color:
                        case_good=False
               if case_good:                          
                  rect_queen=case(i.x,i.y,50,50,surface)
                  pygame.draw.rect(surface,[53,60,255],rect_queen)
                  dernier_move.append(rect_queen)
                  for pion in liste_pion:
                     if fonction(pion.case_pion) ==liste3:
                        case_good=False
                  tempo=liste3
                  tempo[0]-=1
                  liste3=tempo[:]
      case_good=True
      for o in range(8):
         for i in liste_case:
            if liste4==fonction(i.num_case):
               for pion in liste_pion:
                     if fonction(pion.case_pion) ==liste4 and pion.color==self.color:
                        case_good=False
               if case_good:                        
                  rect_queen=case(i.x,i.y,50,50,surface)
                  pygame.draw.rect(surface,[53,60,255],rect_queen)
                  dernier_move.append(rect_queen)
                  for pion in liste_pion:
                     if fonction(pion.case_pion) ==liste4:
                        case_good=False
                  tempo=liste4
                  tempo[1]=int(tempo[1])
                  tempo[1]-=1
                  tempo[1]=str(tempo[1])
                  liste4=tempo[:]
                        
      return dernier_move[:]
class king(pion):
   def __init__(self,left,top,width,height,surface,image,color="black"):
      pion.__init__(self,left,top,width,height,surface,image,color)
      self.king_dead=False
   def show_move(self,surface,liste_case,liste_pion):
      liste1=[self.NcaseX,str(self.NcaseY+1)]
      liste2=[self.NcaseX+1,str(self.NcaseY)]
      liste3=[self.NcaseX-1,str(self.NcaseY)]
      liste4=[self.NcaseX,str(self.NcaseY-1)]
      diago1=[self.NcaseX-1,str(self.NcaseY+1)]
      diago2=[self.NcaseX+1,str(self.NcaseY-1)]
      diago3=[self.NcaseX+1,str(self.NcaseY+1)]
      diago4=[self.NcaseX-1,str(self.NcaseY-1)]

      liste_case_pre=[]
      tempo=[0,0]

      Gigaliste=[liste1[:],liste2[:],liste3[:],liste4[:],diago1[:],diago2[:],diago3[:],diago4[:]]
      dernier_move=[]
      case_good=True
      gigalist2=[]
      diag1=True
      diag2=True
      for e in liste_case:
         #print(fonction(e.num_case),Gigaliste[:])
         if fonction(e.num_case) in Gigaliste[:]:
            for n,a in enumerate(Gigaliste):
               if fonction(e.num_case)==a:
                  for pion in liste_pion:
                     if fonction(pion.case_pion) ==a and pion.color==self.color:
                        case_good=False
                        
                           
                  if case_good:
                     rect_queen=case(e.x,e.y,50,50,surface)
                     pygame.draw.rect(surface,[53,60,255],rect_queen)
                     dernier_move.append(rect_queen)
                  else:
                     case_good=True
      return dernier_move[:]
class cavalier(pion):
   def __init__(self,left,top,width,height,surface,image,color="black"):
      pion.__init__(self,left,top,width,height,surface,image,color)
   def show_move(self,surface,liste_case,liste_pion):
      move1=[self.NcaseX+2,str(self.NcaseY+1)]
      move2=[self.NcaseX+1,str(self.NcaseY+2)]
      move3=[self.NcaseX-2,str(self.NcaseY-1)]
      move4=[self.NcaseX-1,str(self.NcaseY-2)]
      move5=[self.NcaseX-2,str(self.NcaseY+1)]
      move6=[self.NcaseX-1,str(self.NcaseY+2)]
      move7=[self.NcaseX+2,str(self.NcaseY-1)]
      move8=[self.NcaseX+1,str(self.NcaseY-2)]
      Gigaliste=[move1[:],move2[:],move3[:],move4[:],move5[:],move6[:],move7[:],move8[:]]
      dernier_move=[]
      case_good=True
      gigalist2=[]
      diag1=True
      diag2=True
      for e in liste_case:
         #print(fonction(e.num_case),Gigaliste[:])
         if fonction(e.num_case) in Gigaliste[:]:
            for n,a in enumerate(Gigaliste):
               if fonction(e.num_case)==a:
                  for pion in liste_pion:
                     if fonction(pion.case_pion) ==a and pion.color==self.color:
                        case_good=False
                        
                           
                  if case_good:
                     rect_queen=case(e.x,e.y,50,50,surface)
                     pygame.draw.rect(surface,[53,60,255],rect_queen)
                     dernier_move.append(rect_queen)
                  else:
                     case_good=True
      return dernier_move[:]

            




            



               

if __name__=="__main__":
   class test:
      def __init__(self):
         self.pute=0
   toto=test()
   if type(toto)==test:
      print("yes")
   else:
      print("no")
