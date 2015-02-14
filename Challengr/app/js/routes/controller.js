import { Controller } from 'marionette';
import Layout from '../commons/layout';

import MainPage from '../pages/mainPage';
import ImportPage from '../pages/importPage';


export default Controller.extend({
	defaultRoute(){
		Layout.main.show( new MainPage() );
	},
	import(){
		Layout.main.show( new ImportPage() );
	}
});