import { ItemView } from 'marionette';

let Nav = ItemView.extend({
	template: require('__templates__/commons/nav.hbs'),
	tagName: 'nav',
	className: 'navbar navbar-default'
});

export default new Nav();