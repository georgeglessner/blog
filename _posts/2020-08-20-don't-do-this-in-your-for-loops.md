---
layout: post
title: "Don't Do This In Your For Loops"
tags: 
---

Our intern got a ticket yesterday about a page that wouldn't load for one of our employees. The page is a table that displays equipment data. In this case, there were 17,000 lines of equipment that needed to be displayed. But all she saw was a never ending loading circle. 

I took a look at the code, found where the table creation logic was, and saw the following (pseudo-ish code)

```php
$equipmentArray = getEquipmentArray($location); // 17,000 entries
$equipmentChunk = array_chunk($equipmentArray, 500); // 34 chunks

for ($i=0; $i<count($equipmentChunk); $i++){
    // some logic here 

    for($j=0; $j<count($equipmnetChunk[$i]); $j++) {
        // table logic here
    }
}
```

The common issue that was made here was calling `count()` inside the for loop iteration. To optimize this code, it would be better to write it as such

```php
$equipmentArray = getEquipmentArray($location); // 17,000 entries
$equipmentChunk = array_chunk($equipmentArray, 500); // 34 chunks
$chunkCount = count($equipmentChunk);

for ($i=0; $i<$chunkCount; $i++){
    // some logic here 
    $equipmentDetail = $equipmnetChunk[$i];
    $equipmnetCount = count($equipmentDetail);
    
    for($j=0; $j<$equipmentCount; $j++) {
        // table logic here
    }
}
```

By calling the `count()` functions outside of the iterations, this ***greatly*** reduces the execution time. Before, `count()` was being called 17,034 times in this scenario. With the new implementation, `count()` is only being called 35 times. 

Another way of solving this issue would be to use a `foreach()` loop. The `foreach()` loop does the calculation of the iteration size for you so you don't need to use `count()` at all. An example of the above scenario using a `foreach()` loop would look something like the following

```php
$equipmentArray = getEquipmentArray($location); // 17,000 entries
$equipmentChunk = array_chunk($equipmentArray, 500); // 34 chunks

foreach($equipmnetChunk as $chunk){
    // some logic here 
    
    foreach($chunk) {
        // table logic here
    }
}
```

As you can see, this is a very easy to read solution. I was able to remove all `count()` calculations, and only had to use the `$equipmentChunk` variable to get all the data. 

Whichever way you prefer to do iteration, just be sure you are not calculating your iteration size every iteration. Instead, calculate the size beforehand and you will save yourself a lof of resources and time! 