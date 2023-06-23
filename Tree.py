''' '''
Families={
    'charley':
    {
        'sam':{'Boxy','Rosy'},'Nila':{'Pepsi'}
    },
    'Devi':{
        'Tommy':{'Tony'},
        'Timmy':{'Hamster'},
        'Tammy':{'Hamster'}
    },
    'carlos':
    
        {'Diego':'cat','Ferret':'Fox'}
    
}
for parent,children in Families.items():
    print(f"{parent} has {len(children)} kid(s):")
    print(f"{', and '.join(str(i) for i in{*children})}")
    '''
    1)LEVEL ORDER TRAVERSEL:you traverse level by level by left to right.
    2)DEPTH ORDER TRAVERSEL:
    ->INORDER(Left,Root,Right)
    ->PREORDER(Root,Left,Right)
    ->POSTORDER(Left,Right,Root)
    700,400,900,600,100,800,500,300,200
    100,400,700,600,900,500,800,200,300
    700,900,600,400,800,300,200,500,100'''