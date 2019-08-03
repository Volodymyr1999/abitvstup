$(function () {

    		var items = $('.slide-item');
			left = 0;
			for(var i=0;i<items.length;i++){
				items[i].style.left = left+'%';
				left+=100;
    		}

		});
		$('.controller').click(function () {
			var width = 100;
			var index = $('.active').index();
			if(index<$(this).index()){
				while(index<$(this).index()) {
					$('.slide-item').animate({'left': '-=value%'.replace('value', width)}, 500);
					index++;
				}

			}
			else if(index>$(this).index()){
				while(index>$(this).index()) {
					$('.slide-item').animate({'left': '+=1300px'.replace('value', width)}, 500);
					index--;
				}
			}
			$('.active').removeClass('active');
			$(this).addClass('active');

		});
