function modalContentChange(district){

  var districtName = "";
  var zips = [];
  var neighborhoods = [];
  var uniqueZips = [];

  // document.getElementById("zipcodes").innerHTML = "";
  document.getElementById("listingprice").innerHTML = "";
  $('#neighborhood').empty();
  document.getElementById("daysinmarket").innerHTML = "";
  
    d3.json("/districts_beats", function(data) {
      data.filter(function(d){
      
        if (d.district == district ){

          districtName = d.district_name;

          d3.select('#safetyranking').html("");
          d3.select('#safetyranking2').html("");


          // var elem = document.createElement("img");
          var src = `../static/img/district${district}.jpg`;
          // elem.src = `../static/img/district${district}.jpg`;
          // elem.classList.add = 'img-thumbnail-xx';

          d3.select('#safetyranking')
          .append('img')
          .attr('class', 'img-thumbnail-xx')
          .attr('src', src);

          var topCounter = 0;
          for ( i=0; i<beatCrimeCount2.length; i++ ){
            for ( j=0; j<beatCrimeCount2[i].length; j++ ){
              if (beatCrimeCount2[i][j][0] == district){

                  beatInfo = data.filter(function(d){ return (d.beat == beatCrimeCount2[i][j][1] && d.district == district) })
                  
                  topCounter++;

                  // d3.select('#safetyranking')
                  // .append('br');
                  d3.select('#safetyranking2')
                  .append('br');


                  d3.select('#safetyranking2')
                  .append("h5").text('#' + topCounter + ' Beat ' + beatCrimeCount2[i][j][1] + ' - ' + beatInfo[0].neighborhood);

                  d3.select('#safetyranking2')
                  .append("h6").text('Crime Count : ' + beatCrimeCount2[i][1]);

                }
              }
            }
          }
        })

      // Sets the district's overview title
      d3.select('#overview-title').html("");
      d3.select('#overview-title')
          .append("h2").text(`District ${district}: ${districtName} | Overview`);

    });

    d3.json("/districts_zip", function(data) {
      

      district_zips = data.filter(function(d){ return (d.district == district)})

      // zips.push(district_zips.Zip_Code);
      // neighborhoods.push(district_zips.neighborhood);

      // var sel = document.getElementById('neighborhood');

      // neighborhoods.forEach(function(item){
      //   // document.getElementById("neighborhoods").innerHTML += `${item} `;        

      //   // create new option element
      //   var opt = document.createElement('option');

      //   // create text node to add to option element (opt)
      //   opt.appendChild( document.createTextNode(`${item.neighborhood}`) );

      //   // set value property of opt
      //   opt.value = `${item.neighborhood}`; 

      //   // add opt to end of select box (sel)
      //   sel.appendChild(opt); 

      //   console.log(item.neighborhood);

      // });

      var sel = document.getElementById('neighborhood');

      district_zips.forEach(function(item) {
        neighborhoods.push(item.neighborhood);

        var opt = document.createElement('option');

          // create text node to add to option element (opt)
          opt.appendChild( document.createTextNode(`${item.district}${item.beat} ${item.neighborhood}`) );
  
          // set value property of opt
          opt.value = `${item.district}${item.beat}`; 
  
          // add opt to end of select box (sel)
          sel.appendChild(opt); 

      })

      console.log(neighborhoods);

      // var unique = function(xs) {
      //   return xs.filter(function(x, i) {
      //     return xs.indexOf(x) === i
      //   })
      // };

      // uniqueZips = unique(zips);

      // uniqueZips.forEach(function(item){
      //   // document.getElementById("zipcodes").innerHTML += `${item} `;
      // });

    });

    d3.json("/sac_realestate", function(data) {

      realEstate = data.filter(function(d){ return (d.district == district)});

      var medListingPrice = d3.median(realEstate, function(d) { return d.price; });
      medListingPrice = numberWithCommas(medListingPrice);
      document.getElementById("listingprice").innerHTML = `$ ${medListingPrice} `;

      console.log(data);
      

      // var avgDaysInMarket = d3.mean(realEstate, function(d) { return d.median_days_on_market; });
      // avgDaysInMarket = avgDaysInMarket.toFixed(2);
      // document.getElementById("daysinmarket").innerHTML = `${avgDaysInMarket} `;

      function numberWithCommas(x) {
        return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
      }


    });


    // d3.json("/realestate", function(data) {

    //   // realEstate = data.filter(function(d){ return (uniqueZips.includes(d.postal_code))});

    //   // var medListingPrice = d3.median(realEstate, function(d) { return d.median_listing_price; });
    //   // medListingPrice = numberWithCommas(medListingPrice);
    //   // document.getElementById("listingprice").innerHTML = `$ ${medListingPrice} `;
      

    //   // var avgDaysInMarket = d3.mean(realEstate, function(d) { return d.median_days_on_market; });
    //   // avgDaysInMarket = avgDaysInMarket.toFixed(2);

    //   realEstate = data.filter(function(d){ return (d.district == district)})

    //   var medListingPrice = d3.median(realEstate, function(d) { return d.price; });
    //   medListingPrice = numberWithCommas(price);
    //   document.getElementById("listingprice").innerHTML = `$ ${medListingPrice} `;
      

    //   // var avgDaysInMarket = d3.mean(realEstate, function(d) { return d.median_days_on_market; });
    //   // avgDaysInMarket = avgDaysInMarket.toFixed(2);
    //   // document.getElementById("daysinmarket").innerHTML = `${avgDaysInMarket} `;

    //   function numberWithCommas(x) {
    //     return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    //   }

    //   function numberWithCommas(x) {
    //     return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    //   }

    //   document.getElementById("listingprice").innerHTML = `$${numberWithCommas(data.toFixed(2))} `;

    //   console.log(data);

      

    //   // document.getElementById("daysinmarket").innerHTML = 'hhihihi';

    //   // function numberWithCommas(x) {
    //   //   return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    //   // }

    // });


    

}


function pass_values() {
  var e = document.getElementById("neighborhood");
  var beat = e.options[e.selectedIndex].value;

  var beds = document.getElementById("beds").value;
  var baths = document.getElementById("baths").value;


  $.ajax(
    {
      type:'POST',
      contentType:'application/json;charset-utf-08',
      dataType:'json',
      url:`http://127.0.0.1:5000/pass_val?beat=${beat}&beds=${beds}&baths=${baths}`,
      success:function (data) {

        console.log(data);

        function numberWithCommas(x) {
          return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
        }
  
        document.getElementById("listingprice2").innerHTML = `$${numberWithCommas(data.toFixed(2))} `;
  
        console.log(data);
          // var reply=data.reply;
          // if (reply=="success")
          // {
          //   console.log("success");
          //   return;


              
          // }
          // else
          //     {
          //     alert("some error ocured in session agent")
          //     }

      }
    }
  );

  // d3.json("/pass_val", function(data) {
  //   console.log(data);
  // });

  

   
}


