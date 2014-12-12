select concat(is_location,',',share,',',comment,
	',',like_number,',',vdo,',',image,',',url,
	',',tags_number) 
from feature_model into outfile '/tmp/fselect.txt';
