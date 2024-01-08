N='Invalid input, please try again'
M='Enter the number associated with the action: \n'
X='yes'
L='none'
J=float
K=round
G='-----------------------------------------------------------------'
B=input
D=int
C=str
A=print
A('\n┏┳┓┓     ┏┓     ┏┓┏  ┏┳┓┓     ┏┓          ')
A(' ┃ ┣┓┏┓  ┣┫┏┓╋  ┃┃╋   ┃ ┣┓┏┓  ┣ ┏┓┏╋┏┓┏┓┓┏')
A(' ┻ ┛┗┗   ┛┗┛ ┗  ┗┛┛   ┻ ┛┗┗   ┻ ┗┻┗┗┗┛┛ ┗┫')
A('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ')
A('                                             ')
import math as E
list=[L,2,L,X,.0,51]
def H(array):
	L=array;Y=L[0];M=L[1];W=L[2];j=L[3];k=L[4];R=L[5];H=3;I=16;J=12;F=6;N=40;S=R*2.5;Z=R*3;v=D(E.ceil(S/F));w=D(E.ceil(Z/I));x=D(E.ceil(S/J));y=D(E.ceil(F/H));l=.2;m=.45;n=.7;o=1.2;p=1.7;O=2.25;P=1.5;a=.4;b=.2;q=.35;B=1.
	if Y=='communism':H=H*O;I=I*O;F=F*O;J=J*O;N=N*O
	elif Y=='socialism':H=H*P;I=I*P;F=F*P;J=J*P;N=N*P
	A('')
	if M==1:B=B+l
	elif M==2:B=B+m
	elif M==3:B=B+n
	elif M==4:B=B+o
	elif M==5:B=B+p
	else:B=B+0
	if j==X:B=B+q
	else:B=B+0
	A(G)
	if W=='forced labor':B=B+a
	elif W=='public service':B=B+b
	elif W=='both':B=B+b+a
	else:B=B+0
	A('');B=B+k/100;c=S/(F*B);r=S/(J*B);s=Z/(I*B);t=c/(H*B);T=D(E.ceil(c));U=D(E.ceil(r));V=D(E.ceil(s));Q=D(E.ceil(t));d=T*2+.1;e=U*3.5+.1;f=V*2+.1;g=Q*4+.1;h=Q*.2+.1;i=(T+V+U+Q+R)*250000;u=d*96000+f*96000+e*41500+g*38000+h*102000;A('Motor factory makes about: '+C(K(F*B,2))+' motor parts');A('Electronics factory makes about: '+C(K(I*B,2))+' electronics');A('Fertilizer factory makes about: '+C(K(J*B,2))+' fertilizers');A('Steel factory makes about: '+C(K(H*B,2))+' steel');A('Civilian factory makes about: '+C(K(N*B,2))+' consumer goods');A(f"Cost to build everything: {25000000*(T+U+V+Q+R):,}");A('\nYou need: \n'+C(T)+' motor factories \n'+C(V)+' electronic factories \n'+C(U)+' fertilizer factories \n'+C(Q)+' steel factories \n');A('Resources you need: \n'+C(d)+' Tungsten \n'+C(f)+' Copper and Gold \n'+C(e)+' Phosphate \n'+C(g)+' Iron \n'+C(K(h,2))+' Titanium \n');A('Good luck LMAO');A(f"Your resource income is: {i:,}");A(f"Your actual income is: {i-u:,}")
def O():H(list)
def I():A=C(B('\nIdeology? \n'));E=D(B('Factory output? (0-5) \n'));F=C(B('What policy? (forced labor, public service, both or none)\n'));G=C(B('Do you have Ignore safety Regulations? (Yes/No)\n'));H=J(B('Enter any custom factory modifiers in a percentage. Put 0 if there are none. (25% = 25) \n'));I=J(B('Civilian factory count? \n'));list[0]=A;list[1]=E;list[2]=F;list[3]=G;list[4]=H;list[5]=I
def P():
	C=0
	while C!=5:
		A(M);A('(1) Factory spam!');A('(2) Resource policies');A('(3) How many factories do I need for X amount of Y');A('(4) Change modifiers');A('(5) Return to menu');C=D(B())
		if C==1:H(list);A(G)
		elif C==2:A(2);A(G)
		elif C==3:A(3);A(G)
		elif C==4:I();A(G)
		elif C==5:A('You have returned to menu.')
		else:A(N)
F=0
while F!=3:
	A(M);A('(1) Enter modifiers');A('(2) Run a Test');A('(3) Quit\n');F=D(B())
	if F==1:I();A(G);P()
	elif F==2:O();A(G)
	elif F==3:A('You have quit.')
	else:A(N)