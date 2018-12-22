var musicBox= {
 
    musicDom : null, //播放器对象
    songs : [],        //歌曲目录，用数组来存储
 
    //初始化音乐盒
    init : function(){
        this.musicDom = document.createElement('audio');
    },
 
    //添加一首音乐
    add : function(src){
        this.songs.push(src);
    },
 
    //根据数组下标决定播放哪一首歌
    play : function(index){
        this.musicDom.src = this.songs[index];
        this.musicDom.play();
    },
 
    //暂停音乐
    stop : function(){
        this.musicDom.pause();
    },
 
    //下一首（待编写）
    next : function(){
 
    },
 
    //上一首（待编写）
    prev : function(){
 
    }
}

musicBox.init(); //初始化
musicBox.add('mp3/2.mp3');
musicBox.play(0); //听第一首歌
