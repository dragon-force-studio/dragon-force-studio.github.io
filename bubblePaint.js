// bubble-paint.js
registerPaint('randomBackground', class {
    paint(ctx, geom) {
        const pseudoRandomInts = [12,21,34,4,55,435,6,54,423,31,231,24,56,34,2,345,234]
      var rectSize = 36;
      for(var x = 0; x < geom.width; x += rectSize)
      for(var y = 0; y < geom.height; y += rectSize){
        /// Fill in random block
        ctx.fillStyle = getPseudoRandomHexColor(pseudoRandomInts[((x*y) / rectSize) % pseudoRandomInts.length]);
        ctx.fillRect(x, y, rectSize, rectSize);
      }
    
    }
  })
  
  function getRandomHexColor() {
      var arr = ["rgb(14, 14, 14)","rgb(20, 20, 20)", "rgb(24, 24, 24)"];
    return arr[Math.floor(Math.random() * arr.length)]; 
  }  
  function getPseudoRandomHexColor(index) {
    var arr = ["rgb(129, 19, 19)","rgb(180, 23, 23)", "rgb(158, 23, 23)"];
  return arr[index % arr.length]; 
    }