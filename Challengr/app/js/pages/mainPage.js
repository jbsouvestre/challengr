import { ItemView } from 'marionette';

let RootPage = ItemView.extend({
	template: require('__templates__/pages/mainPage.hbs')
});

export default RootPage;