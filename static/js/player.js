var ap = new APlayer({
    element: document.getElementById('player1'),                       // Optional, player element
    narrow: false,                                                     // Optional, narrow style
    autoplay: false,                                                    // Optional, autoplay song(s), not supported by mobile browsers
    showlrc: 1,                                                        // Optional, show lrc, can be 0, 1, 2, see: ###With lrc
    mutex: true,                                                       // Optional, pause other players when this player playing
    theme: '#444',                                                  // Optional, theme color, default: #b7daff
    mode: 'random',                                                    // Optional, play mode, can be `random` `single` `circulation`(loop) `order`(no loop), default: `circulation`
    preload: 'metadata',                                               // Optional, the way to load music, can be 'none' 'metadata' 'auto', default: 'auto'
    listmaxheight: '128px',                                             // Optional, max height of play list
    music: [
        {
            title: 'あっちゅ～ま青春!',
            author: '七森中☆ごらく部',
            url: 'https://moeplayer.b0.upaiyun.com/aplayer/yuruyuri.mp3',
            pic: 'https://moeplayer.b0.upaiyun.com/aplayer/yuruyuri.jpg'
        },
        {
            title: 'secret base~君がくれたもの~',
            author: '茅野愛衣',
            url: 'https://moeplayer.b0.upaiyun.com/aplayer/secretbase.mp3',
            pic: 'https://moeplayer.b0.upaiyun.com/aplayer/secretbase.jpg'
        },
        {
            title: '回レ！雪月花',
            author: '小倉唯',
            url: 'https://moeplayer.b0.upaiyun.com/aplayer/snowmoonflowers.mp3',
            pic: 'https://moeplayer.b0.upaiyun.com/aplayer/snowmoonflowers.jpg'
        }
    ]
});
