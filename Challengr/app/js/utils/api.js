var baseUrl = '/api';

export default {
	baseUrl: baseUrl,

	url: function(url){
		return [ baseUrl + url ].join('/');
	}
};