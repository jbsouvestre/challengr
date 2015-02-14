import { Controller } from 'marionette';
import Layout from '../commons/layout';

import MainPage from '../pages/mainPage';
import ImportPage from '../pages/importPage';
import ProfileView from '../pages/profileView';

export default Controller.extend({
    defaultRoute(){
        Layout.main.show( new MainPage() );
    },
    register(){
        //Layout.main.show( new RegisterView() );
    },
    viewProfile(id){
        Layout.main.show( new ProfileView(id) );
    },
    createAi(){
        //Layout.main.show( new CreateAIView(id) );
    },
    import(){
        Layout.main.show( new ImportPage() );
    }
});